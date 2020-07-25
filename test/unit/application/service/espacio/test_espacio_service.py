from src.app.domain.model.bodega.bodega import Bodega
from src.app.infrastructure.domain.bodega.in_memory.in_memory_bodega_repository import InMemoryBodegaRepository
from src.app.infrastructure.domain.espacio.in_memory.in_memory_espacio_repository import InMemoryEspacioRepository
from src.app.application.service.espacio.espacio_service import EspacioService

def test_find_bodega_should_return_a_warehouse():
    bodega_init=Bodega("bodega_inicial")
    bodega_repository=InMemoryBodegaRepository()
    bodega_repository.append(bodega_init)
    espacio_service=EspacioService(bodega_repository, InMemoryEspacioRepository())
    bodega_test=espacio_service.find_bodega(bodega_init.get_id())
    assert bodega_test.get_name()==bodega_init.get_name()