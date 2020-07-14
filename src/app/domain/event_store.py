import abc
from src.app.domain.model.shared.event import Event

class EventStore(abc.ABC):

    @abc.abstractmethod
    def append(self, event:Event):
        pass
    
    @abc.abstractmethod
    def all_events_since(self, event_id:int):
        pass