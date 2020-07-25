from src.app.infrastructure.domain.bodega.in_memory.in_memory_bodega_repository import InMemoryBodegaRepository
from src.app.domain.model.bodega.bodega import Bodega


def test_bodega_repository_append_bodega():
    repo=InMemoryBodegaRepository()
    repo.append(Bodega("bodega-123"))
    assert repo.number_elements()==1

def test_bodega_repository_find_by_id():
    repo=InMemoryBodegaRepository()
    bodega=Bodega("bodega-123")
    bodega2=Bodega("bodega-2")
    bodega_id=bodega.get_id()
    bodega_id2=bodega2.get_id()
    repo.append(bodega)
    bodega_test=repo.find_by_id(bodega_id)
    bodega_test2=repo.find_by_id(bodega_id2)
    assert bodega is bodega_test
    assert bodega_test2 is None

def test_bodega_repository_find_by_name():
    repo=InMemoryBodegaRepository()
    bodega=Bodega("bodega-123")
    repo.append(bodega)
    bodega_test=repo.find_by_name("bodega-123")
    bodega_test2=repo.find_by_name("bodega-321")
    assert bodega is bodega_test
    assert bodega_test2 is None