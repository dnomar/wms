from src.app.domain.model.shared.domain_event_publisher import DomainEventPublisher 
from src.app.domain.model.espacio.espacio_created import EspacioCreated


class Espacio:
    
    def __init__(self, name:str, max_volume:int, max_weight:int,warehouse_id:str):
        self._name = name
        self._max_vol = max_volume
        self._max_weight = max_weight
        self._products = []
        self._warehouse_id = warehouse_id
        self._publish_event()
    
    
    def _publish_event(self):
        DomainEventPublisher().publish(EspacioCreated(self._name))