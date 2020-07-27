import sys
sys.path.append(r"C:\Users\vlonc_000\Documents\08 Code\wms")
from src.app.infrastructure.domain.bodega.in_memory.in_memory_bodega_repository import InMemoryBodegaRepository
from src.app.infrastructure.domain.espacio.in_memory.in_memory_espacio_repository import InMemoryEspacioRepository
from src.app.application.service.espacio.new_space_usecase import NewSpaceUseCase
from src.app.application.service.espacio.allocate_espacio_request import AllocateEspacioRequest
from src.app.domain.model.shared.exceptions import NonExistingWarehouseException, SpaceAlreadyExistException
from src.app.domain.model.bodega.bodega import Bodega
from src.app.infrastructure.domain.event.in_memory.in_memory_event_store import InMemoryEventStore
import pytest


def test_allocate_new_space_succesfully():
    InMemoryEventStore().clear_all()
    bodega_repo = InMemoryBodegaRepository()
    espacio_repo = InMemoryEspacioRepository()
    bodega = Bodega('Bodega-123456')
    wh_id= bodega.get_id()
    space_name = 'space-1'
    space_maximum_volume = 10
    space_maximum_weight = 100  
    bodega_repo.append(bodega)
    resp=NewSpaceUseCase(bodega_repo,espacio_repo).execute(AllocateEspacioRequest(wh_id, space_name, space_maximum_volume, space_maximum_weight))
    assert len(InMemoryEventStore().all_events_since(0)) == 2
    InMemoryEventStore().clear_all()
    assert espacio_repo.number_elements()==1
    assert resp.name() == space_name



def test_allocate_new_space_in_empty_warehouse_throws_NonExistingWarehouseException():
    bodega_repo = InMemoryBodegaRepository()
    espacio_repo = InMemoryEspacioRepository()
    wh_name = 'Bodega-123456'
    space_name = 'space-1'
    space_maximum_volume = 10
    space_maximum_weight = 100  
    with pytest.raises(NonExistingWarehouseException, match=wh_name):
        NewSpaceUseCase(bodega_repo,espacio_repo).execute(AllocateEspacioRequest(wh_name, space_name, space_maximum_volume, space_maximum_weight))
    