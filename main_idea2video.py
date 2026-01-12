import asyncio
from pipelines.idea2video_pipeline import Idea2VideoPipeline


# SET YOUR OWN IDEA, USER REQUIREMENT, AND STYLE HERE
idea = \
    """
A cute British Shorthair blue and white kitten is playing with a bright red yarn ball 
in a cozy, sunlit living room. The kitten pounces on the ball, rolls around with it, 
and occasionally looks at the camera with big, curious eyes. 
The scene is full of joy and playful energy.
"""
user_requirement = \
    """
Short and sweet. No more than 2 scenes, each with 3 shots.
"""
style = "3D Animation Style, Pixar-like, colorful and high quality"


async def main():
    pipeline = Idea2VideoPipeline.init_from_config(
        config_path="configs/idea2video_volc.yaml")
    await pipeline(idea=idea, user_requirement=user_requirement, style=style)

if __name__ == "__main__":
    asyncio.run(main())
