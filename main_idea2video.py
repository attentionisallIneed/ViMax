import asyncio
from pipelines.idea2video_pipeline import Idea2VideoPipeline


# SET YOUR OWN IDEA, USER REQUIREMENT, AND STYLE HERE
idea = \
    """
拍摄一个苏联笑话的视频，这个笑话讲的是：
在苏联，一位外国人问一个苏联公民：“你们这里言论自由吗？”
苏联人回答：“当然自由！我们可以随便批评美国总统、英国首相、法国总统……想怎么骂就怎么骂！”
外国人惊讶：“那你们能批评苏联领导人吗？”
苏联人立刻压低声音：“嘘！你疯了？我们这儿可没有那么自由！”
"""
user_requirement = \
    """
幽默诙谐，场景在苏联街头，有苏联特色的建筑和服装
"""
style = "Soviet-style, colorful and high quality"


async def main():
    pipeline = Idea2VideoPipeline.init_from_config(
        config_path="configs/idea2video_volc.yaml")
    await pipeline(idea=idea, user_requirement=user_requirement, style=style)

if __name__ == "__main__":
    asyncio.run(main())
