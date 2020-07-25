from src.app.adapters.message import AbstracMessage
from test import randoms


class FakeMail(AbstracMessage):
    _instance = None
    _mail_stack = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls, *args, **kwargs)
            cls._mail_stack = []
        return cls._instance

    def send(self, contact: str, body: str):
        self._mail_stack.append([
            {
                "msg_id": f"{randoms.random_suffix()}-{randoms.random_suffix()}-{randoms.random_suffix()}",
                "to": contact,
                "msg_body": body
            },
        ])

    def get_mailstack(self):
        return self._mail_stack

