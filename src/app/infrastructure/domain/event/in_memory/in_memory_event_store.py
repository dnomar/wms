from src.app.domain.event_store import EventStore
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
        self._event_store.append(event)
    
    def all_events_since(self, event_id:int):
        return self._event_store




