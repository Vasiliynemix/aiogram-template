from src.bot.keyboards.register import RegisterKeyboard
from src.bot.lexicon.lexicon import LexiconMsgKbName


class Keyboard:
    def __init__(self, kb_name: LexiconMsgKbName) -> None:
        self._kb_name = kb_name
        self.register_kb = RegisterKeyboard(self._kb_name)
