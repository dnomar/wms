from src.app.infrastructure.domain.bodega.in_memory.in_memory_bodega_repository import InMemoryBodegaRepository
from src.app.domain.model.bodega.bodega import Bodega


def test_bodega_repository_append_bodega():
    repo=InMemoryBodegaRepository()
    repo.clear_all()
    repo.append(Bodega("bodega-123"))
    assert repo.number_elements()==1
    repo.clear_all()

def test_bodega_repository_find_by_id():
    repo=InMemoryBodegaRepository()
    repo.clear_all()
    bodega=Bodega("bodega-123")
    bodega2=Bodega("bodega-2")
    bodega_id=bodega.get_id()
    bodega_id2=bodega2.get_id()
    repo.append(bodega)
    bodega_test=repo.find_by_id(bodega_id)
    bodega_test2=repo.find_by_id(bodega_id2)
    assert bodega is bodega_test
    assert bodega_test2 is None
    repo.clear_all()

def test_bodega_repository_find_by_name():
    repo=InMemoryBodegaRepository()
    repo.clear_all()
    bodega=Bodega("bodega-123")
    bodega2=Bodega("bodega-2")
    bodega3=Bodega("bodega-3")
    repo.append(bodega)
    repo.append(bodega2)
    repo.append(bodega3)
    bodega_test=repo.find_by_name("bodega-123")
    bodega_test2=repo.find_by_name("bodega-321")
    assert bodega is bodega_test
    assert bodega_test2 is None
    repo.clear_all()

def test_bodega_repository_singleton_behavior():
    repo1 = InMemoryBodegaRepository()
    repo1.append(Bodega("bodega-1-sing"))
    repo1.append(Bodega("bodega-2-sing"))
    repo1.append(Bodega("bodega-3-sing"))
    repo2 = InMemoryBodegaRepository()
    assert repo1 is repo2
    assert repo2.number_elements()==3
    repo1.clear_all()
    assert repo2.number_elements()==0
    