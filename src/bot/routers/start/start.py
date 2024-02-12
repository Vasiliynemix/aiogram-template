from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery

from src.bot.filters.filters import MainMenuKBReplyFilter
from src.bot.keyboards.keyboards import Keyboard
from src.bot.keyboards.register import MainMenuData, MainMenuActions
from src.bot.lexicon.lexicon import Lexicon

router = Router()


@router.message(CommandStart())
async def start(message: Message, lexicon: Lexicon, kb: Keyboard) -> None:
    await message.answer(
        lexicon.send.on_start_register, reply_markup=kb.register_kb.on_main_menu_mp()
    )


@router.message(MainMenuKBReplyFilter())
async def main_menu(message: Message, lexicon: Lexicon, kb: Keyboard) -> None:
    await message.answer(
        lexicon.send.on_main_menu_click,
        reply_markup=kb.register_kb.on_main_menu_inline_mp(),
    )


@router.callback_query(MainMenuData.filter(F.action == MainMenuActions.main_menu))
async def main_menu_click(
    callback: CallbackQuery, lexicon: Lexicon, kb: Keyboard
) -> None:
    await callback.message.delete_reply_markup()
    await callback.message.answer(
        lexicon.send.on_main_menu_click,
        reply_markup=kb.register_kb.on_main_menu_mp(),
    )


@router.callback_query(MainMenuData.filter(F.action == MainMenuActions.back))
async def back_to_main_menu_click(
    callback: CallbackQuery, lexicon: Lexicon, kb: Keyboard
) -> None:
    await callback.answer()
