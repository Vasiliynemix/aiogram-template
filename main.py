import asyncio

from aiogram import Bot
from loguru import logger

from pkg.logging import Logger
from src.bot.bot import TgBot
from src.bot.lexicon.lexicon import Lexicon, LEXICON
from src.bot.routers.routers import routers
from src.config import Config
from src.storage.db.connect import DBConnect
from src.storage.redis.conect import RedisConnect
from src.storage.storage import Storage


async def main() -> None:
    cfg = Config()

    log = Logger(
        log_level=cfg.log_level,
        log_dir_name=cfg.paths.log_dir_name,
        info_log_path=cfg.paths.info_log_path,
        debug_log_path=cfg.paths.debug_log_path,
    )
    log.setup_logger()
    logger.info("setup logger")
    logger.debug("debug is ON")

    bot = Bot(token=cfg.bot.token)

    storage = Storage(
        db=DBConnect(cfg.db.build_connection_str),
        redis=RedisConnect(cfg),
    )

    lexicon = Lexicon(LEXICON)

    tg_bot = TgBot(bot, storage, lexicon)
    tg_bot.set_routers(routers)
    tg_bot.set_cfg(cfg)

    await asyncio.gather(tg_bot.run())


if __name__ == "__main__":
    asyncio.run(main())
