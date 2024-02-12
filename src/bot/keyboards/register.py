from enum import IntEnum, auto

from aiogram.filters.callback_data import CallbackData
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

from src.bot.lexicon.lexicon import LexiconMsgKbName


class MainMenuActions(IntEnum):
    main_menu = auto()
    back = auto()


class MainMenuData(CallbackData, prefix="main_menu"):
    action: MainMenuActions


class RegisterKeyboard:
    def __init__(self, kb_name: LexiconMsgKbName) -> None:
        self._kb_name = kb_name

    def on_main_menu_mp(self, on_one_time: bool = True) -> ReplyKeyboardMarkup:
        builder = ReplyKeyboardBuilder()
        builder.button(text=self._kb_name.main_manu.reply)
        return builder.as_markup(one_time_keyboard=on_one_time, resize_keyboard=True)

    def on_main_menu_inline_mp(self) -> InlineKeyboardMarkup:
        builder = InlineKeyboardBuilder()
        builder.button(
            text=self._kb_name.main_manu.inline,
            callback_data=MainMenuData(action=MainMenuActions.main_menu).pack(),
        )
        builder.button(
            text=self._kb_name.back.inline,
            callback_data=MainMenuData(action=MainMenuActions.back).pack(),
        )
        return builder.as_markup()
