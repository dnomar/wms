from src.app.domain.model.shared.event import Event
from src.app.domain.event_store import EventStore
from  src.app.infrastructure.service.event.dict_event_transformer import DictEventTransformer

class DomainEventSuscriber:

    def __init__(self, repo: EventStore):
        self.repo = repo()

    def add(self, event:Event):
        self.repo.append(DictEventTransformer(event).toDict())