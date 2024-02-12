from aiogram.filters import BaseFilter
from aiogram.types import Message

from src.bot.lexicon.lexicon import Lexicon


class MainMenuKBReplyFilter(BaseFilter):
    async def __call__(self, message: Message, lexicon: Lexicon) -> bool:
        return message.text == lexicon.kb_name.main_manu.reply
