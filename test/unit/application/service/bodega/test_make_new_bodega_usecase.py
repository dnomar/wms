import sys
sys.path.append(r"C:\Users\vlonc_000\Documents\08 code\wms")
from src.app.infrastructure.domain.event.in_memory.in_memory_event_store import InMemoryEventStore
from src.app.domain.model.bodega.bodega import Bodega
from src.app.application.service.bodega.new_bodega_usecase import NewBodegaUseCase
from src.app.application.service.bodega.bodega_request import BodegaRequest
from src.app.infrastructure.domain.bodega.in_memory.in_memory_bodega_repository import InMemoryBodegaRepository


def test_make_new_bodega_usecase():
    repository=InMemoryBodegaRepository()
    repository.clear_all()
    InMemoryEventStore().clear_all()
    new_bodega_uc=NewBodegaUseCase(repository)
    new_bodega_uc.execute(BodegaRequest("bodega-generica-1"))
    new_bodega_uc.execute(BodegaRequest("bodega-generica-2"))
    new_bodega_uc.execute(BodegaRequest("bodega-generica-3"))
    assert repository.number_elements() == 3
    assert len(InMemoryEventStore().all_events_since(0)) == 3
    InMemoryEventStore().clear_all()
    repository.clear_all()
    


#TODO: Exception when add more than one bodega with the same name 