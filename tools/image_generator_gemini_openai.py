import logging
import base64
import io
from typing import List, Optional
from PIL import Image
from openai import OpenAI
from tenacity import retry, stop_after_attempt, wait_fixed
from interfaces.image_output import ImageOutput
from utils.rate_limiter import RateLimiter

class ImageGeneratorGeminiOpenAI:
    def __init__(
        self,
        api_key: str,
        base_url: str,
        model: str = "gemini-3-pro-image",
        rate_limiter: Optional[RateLimiter] = None,
    ):
        self.api_key = api_key
        self.base_url = base_url
        self.model = model
        self.rate_limiter = rate_limiter
        
        self.client = OpenAI(
            api_key=api_key,
            base_url=base_url
        )

    @retry(stop=stop_after_attempt(3), wait=wait_fixed(5))
    async def generate_single_image(
        self,
        prompt: str,
        reference_image_paths: List[str] = [],
        aspect_ratio: Optional[str] = "16:9", # Note: OpenAI API typically handles size, not aspect_ratio directly in all models, but we'll adapt
        size: str = "1024x1024", # Default size usually expected by OpenAI API
        **kwargs,
    ) -> ImageOutput:

        logging.info(f"Calling {self.model} to generate image...")

        # Apply rate limiting if configured
        if self.rate_limiter:
            await self.rate_limiter.acquire()

        # Note: reference_image_paths support depends on the specific model capability via OpenAI API.
        # Standard generic OpenAI image generation (DALL-E 3) doesn't support reference images in the same way.
        # Assuming the custom Gemini endpoint might handle it via prompt or specific parameters if documented,
        # but for now we'll stick to the standard prompt-based generation as per the provided example in gemini_client.py
        
        # If the user script provided (gemini_client.py) didn't use reference images for image gen, we might skip them or append to prompt if possible.
        # But the interface requires it. Let's start with basic prompt.
        
        try:
            # The example user code used:
            # response = client.images.generate(
            #     model="gemini-3-pro-image",
            #     prompt=...,
            #     n=1,
            #     size="1024x1024", 
            #     response_format="b64_json"
            # )

            response = self.client.images.generate(
                model=self.model,
                prompt=prompt,
                n=1,
                size=size, 
                response_format="b64_json"
            )

            if response.data:
                img_data = response.data[0]
                if getattr(img_data, 'b64_json', None):
                    image_data = base64.b64decode(img_data.b64_json)
                    image = Image.open(io.BytesIO(image_data))
                    return ImageOutput(fmt="pil", ext="png", data=image)
                elif hasattr(img_data, 'url') and img_data.url:
                    # If URL is returned, we might need to download it, but let's assume b64_json for now as per test script
                    # For completeness, could add download logic here if needed.
                    import requests
                    resp = requests.get(img_data.url)
                    image = Image.open(io.BytesIO(resp.content))
                    return ImageOutput(fmt="pil", ext="png", data=image)
            
            raise ValueError("No valid image data in response")

        except Exception as e:
            logging.error(f"Image generation failed: {e}")
            raise
