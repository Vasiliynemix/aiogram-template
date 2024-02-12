MAIN_MENU_KB = "Главное меню"
BACK_KB = "Назад"

LEXICON = {
    "msg_send": {
        "on_start_register": "Привет, это первый старт",
        "on_start": "Привет, это обычный старт",
        "on_main_menu_click": MAIN_MENU_KB,
    },
    "msg_kb_name": {
        "main_manu": {
            "reply": MAIN_MENU_KB,
            "inline": MAIN_MENU_KB,
        },
        "back": {
            "reply": BACK_KB,
            "inline": BACK_KB,
        },
    },
}


class Lexicon:
    def __init__(self, lexicon: dict[str, str | dict[str, str]]) -> None:
        self._lexicon = lexicon
        self.send: LexiconMsgSend = LexiconMsgSend(self._lexicon)
        self.kb_name: LexiconMsgKbName = LexiconMsgKbName(self._lexicon)


class LexiconMsgSend:
    def __init__(self, lexicon: dict[str, str | dict[str, str]]) -> None:
        self._lexicon = lexicon["msg_send"]
        self.on_start_register = self._lexicon["on_start_register"]
        self.on_register = self._lexicon["on_start"]
        self.on_main_menu_click = self._lexicon["on_main_menu_click"]


class LexiconMsgKbName:
    def __init__(self, lexicon: dict) -> None:
        self._lexicon = lexicon["msg_kb_name"]
        self.main_manu = LexiconMsgKbNameReplyInline(self._lexicon["main_manu"])
        self.back = LexiconMsgKbNameReplyInline(self._lexicon["back"])


class LexiconMsgKbNameReplyInline:
    def __init__(self, lexicon: dict[str, str | dict[str, str]]) -> None:
        self.reply = lexicon["reply"]
        self.inline = lexicon["inline"]
