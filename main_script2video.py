import asyncio
from pipelines.script2video_pipeline import Script2VideoPipeline


# SET YOUR OWN SCRIPT, USER REQUIREMENT, AND STYLE HERE
script = \
"""
EXT. SCHOOL GYM - DAY
A group of students are practicing basketball in the gym. The gym is large and open, with a basketball hoop at one end and a large crowd of spectators at the other end. Wanggua (18, male, tall, athletic) is the star player, and he is practicing his dribble and shot. Yuyu (17, female, short, athletic) is the assistant coach, and she is helping Wanggua with his practice. The other students are watching the practice and cheering for Wanggua.
Wanggua: (dribbling the ball) I'm going to score a basket!
Yuyu: (smiling) Good job, Wanggua!
Wanggua: (shooting the ball) Yes!
Wanggua:(The shot misses. He seems frustrated.) Argh! My follow-through feels off today.
Yuyu:(Walks over, analytical.) Your elbow is drifting out. Remember, straight as an arrow.
Wanggua:(Nods, taking the ball again.) Straight as an arrow... Let me try again.
(Wanggua takes another shot. This time, the ball swishes through the net perfectly.)
Yuyu:(Clapping.) There it is! Perfect form! That's the shot we need for the championship.
Wanggua:(Retrieving the ball, smiling with renewed confidence.) Thanks, Coach Yuyu. I just needed you to point it out. One more time?
"""
user_requirement = \
"""
Fast-paced with no more than 15 shots.
"""
style = "Anime Style"



async def main():
    pipeline = Script2VideoPipeline.init_from_config(config_path="configs/script2video.yaml")
    await pipeline(script=script, user_requirement=user_requirement, style=style)


if __name__ == "__main__":
    asyncio.run(main())
