import asyncio

from loguru import logger


async def perform():
    """
    只有将异步函数通过asyncio.create_task()包装成Task任务,后续通过asyncio.run()调用才能真正实现异步,只使用await和顺序调用相比没有区别
    """
    logger.info(
        """Perform include talking a joke and washing hands, and washing hands is ahead of the joke,
        it is a part of preparing joke"""
    )
    talk_joke_task = asyncio.create_task(talk_joke())
    wash_hand_task = asyncio.create_task(wash_hand())
    # await talk_joke()·
    # await wash_hand()
    await talk_joke_task
    await wash_hand_task


async def talk_joke():
    print("I am preparing a joke")
    await asyncio.sleep(5)
    print("I am a joke")


async def wash_hand():
    print("I am washing my hands")
    await asyncio.sleep(2)
    print("I have finished washing my hands")


if __name__ == "__main__":
    asyncio.run(perform())
