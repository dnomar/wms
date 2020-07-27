from src.app.domain.model.shared.event import Event
from src.app.infrastructure.domain.event.in_memory.in_memory_event_store import InMemoryEventStore
from src.app.domain.model.shared.domain_event_suscriber import DomainEventSuscriber

#Singleton
class DomainEventPublisher:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls, *args, **kwargs)
            cls._instance.HANDLERS={
                'BodegaCreated':[DomainEventSuscriber(InMemoryEventStore).add],
                'EspacioCreated':[DomainEventSuscriber(InMemoryEventStore).add]
                }
        return cls._instance

  
    def publish(self, event:Event):
        for x in self.HANDLERS:
            if x == event.event_name:
               for y in self.HANDLERS[x]:
                   y(event)

    