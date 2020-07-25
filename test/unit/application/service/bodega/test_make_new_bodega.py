from src.app.infrastructure.domain.event.in_memory.in_memory_event_store import InMemoryEventStore
from src.app.domain.model.bodega.bodega import Bodega
from src.app.application.service.bodega.new_bodega_usecase import NewBodegaUseCase
from src.app.application.service.bodega.bodega_request import BodegaRequest
from src.app.infrastructure.domain.bodega.in_memory.in_memory_bodega_repository import InMemoryBodegaRepository


def test_make_new_bodega_usecase():
    repository=InMemoryBodegaRepository()
    new_bodega=NewBodegaUseCase(repository)
    new_bodega.execute(BodegaRequest("bodega-generica"))
    assert repository.number_elements() == 1
    assert len(InMemoryEventStore().all_events_since(0)) == 1
    InMemoryEventStore().clear_all()
    repository.clear_all()
