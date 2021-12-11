from typing import Optional

from .redis import RedisList

from .model.slack import ErrorMessage, Message


class Logger:
    def __init__(self, channel: str, error_channel: Optional[str] = None):
        self.channel = channel
        self.error_channel = channel if error_channel is None else error_channel
        self.redis = RedisList()

    async def error(self, origin: Optional[str]):
        em = ErrorMessage.from_exc_info(channel=self.error_channel, origin=origin)
        await self.redis.lpush("slack", em)

    async def info(self, message: str, mention: bool = False):
        m = Message(channel=self.channel, message=message, mention=mention)
        await self.redis.lpush("slack", m)
