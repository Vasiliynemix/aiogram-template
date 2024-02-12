from aiogram.fsm.storage.redis import RedisStorage
from redis.asyncio import Redis

from src.config import Config


class RedisConnect:
    def __init__(self, cfg: Config) -> None:
        self._cfg = cfg
        self._redis = None

    async def set_redis(self) -> None:
        self._redis = Redis(
                    db=self._cfg.redis.db,
                    host=self._cfg.redis.host,
                    password=self._cfg.redis.passwd,
                    username=self._cfg.redis.username,
                    port=self._cfg.redis.port,
                )

    async def get_redis_storage(self) -> RedisStorage:
        return RedisStorage(redis=self._redis, state_ttl=self._cfg.redis.state_ttl, data_ttl=self._cfg.redis.data_ttl)
