import asyncio
import os

# Set NO_PROXY to avoid 502 errors with local services
os.environ["NO_PROXY"] = "127.0.0.1,localhost"

from pipelines.idea2video_pipeline import Idea2VideoPipeline


# SET YOUR OWN IDEA, USER REQUIREMENT, AND STYLE HERE
idea = \
    """
    一个少女下雨的城市霓虹下行走，然后坐在积水的路边，打开一罐冷饮。
    当她抬头的时候，看到远处的广告牌亮起，上面跳出一行字：“鱼鱼，加油！”
    少女受到鼓舞，欣慰的笑了。镜头特写，她的眼里浮现出泪光。
    """
user_requirement = \
    """
    赛博朋克风格 (Cyberpunk style)。
    环境：雨夜，充满霓虹灯光的街道，潮湿的路面反射着彩色光芒，远处有全息广告牌。
    人物：少女，衣着现代或带有未来感。
    氛围：孤独但随后感到温暖和希望。
    画面：电影质感，高清晰度，光影效果丰富。
    """
style = "Cyberpunk Style, Neon Lights, Rainy City, Cinematic Lighting, High Quality"


async def main():
    pipeline = Idea2VideoPipeline.init_from_config(
        config_path="configs/idea2video_volc.yaml")
    await pipeline(idea=idea, user_requirement=user_requirement, style=style)

if __name__ == "__main__":
    asyncio.run(main())
