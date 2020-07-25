from src.app.domain.model.bodega.bodega_id import BodegaId
from src.app.domain.model.bodega.bodega_created import BodegaCreated
from src.app.domain.model.shared.domain_event_publisher import DomainEventPublisher


class Bodega:

    def __init__(self, name:str):
        self._id=BodegaId.next_identity()
        self._name=name
        self._publish_event()

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name
    
    def _publish_event(self):
        DomainEventPublisher().publish(BodegaCreated(self._id))

    #TODO: Pending .build to raise an Event


