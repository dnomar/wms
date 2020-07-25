from src.app.domain.model.shared.event import Event
from src.app.domain.event_store import EventStore

class DomainEventSuscriber:

    def __init__(self, repo: EventStore):
        self.repo = repo()

    def add(self, event:Event):
        self.repo.append(event)