from src.app.domain.event_store import EventStore
from src.app.infrastructure.service.event.dict_event_transformer import DictEventTransformer
from src.app.domain.events import Event

#Singleton
class InMemoryEventStore(EventStore):
    _instance = None
 
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls, *args, **kwargs)
            cls._instance._event_store=[]
        return cls._instance
    
    def append(self, event:Event):
        dict_event=DictEventTransformer(event)
        self._event_store.append(dict_event)
    
    def all_events_since(self, event_id:int):
        events_since=[x for x in self._event_store if self._event_store.index(x)>=event_id]
        return events_since

    def get_event(self, event_id:int):
        return self._event_store[event_id]



