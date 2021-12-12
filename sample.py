import asyncio
from redis_push import Logger


logger = Logger(channel="test")


async def main():
    try:
        1 / 0
    except Exception:
        await logger.error(origin="sample")

    await logger.info(message="*テスト*")
    await logger.close()


asyncio.run(main())
