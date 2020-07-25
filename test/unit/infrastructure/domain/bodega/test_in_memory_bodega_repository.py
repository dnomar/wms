from src.app.infrastructure.domain.bodega.in_memory.in_memory_bodega_repository import InMemoryBodegaRepository
from src.app.domain.model.bodega.bodega import Bodega


def test_bodega_repository_append_bodega():
    repo=InMemoryBodegaRepository()
    repo.append(Bodega("bodega-123"))
    assert repo.number_elements()==1

def test_bodega_repository_find_by_id():
    repo=InMemoryBodegaRepository()
    bodega=Bodega("bodega-123")
    bodega_id=bodega.get_id()
    repo.append(bodega)
    bodega_test=repo.find_by_id(bodega_id)
    print(bodega)
    print(bodega_test)
    assert bodega is bodega_test
