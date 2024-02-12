from src.storage.db.connect import DBConnect
from src.storage.redis.conect import RedisConnect


class Storage:
    def __init__(self, db: DBConnect, redis: RedisConnect) -> None:
        self._db = db
        self._redis = redis

    @property
    def db(self) -> DBConnect:
        return self._db

    @property
    def redis(self) -> RedisConnect:
        return self._redis
