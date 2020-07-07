from src.app.adapters.repository import AbstractRepository
from src.app.domain import events


class FakeLogginRepository(AbstractRepository):

    def __init__(self):
        self.events = []

    def add(self, event: events.Event):
        self.events.append(event)

    def get(self, reference: str):
        pass

    def get_all(self):
        return self.events