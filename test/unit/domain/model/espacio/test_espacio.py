from src.app.domain.model.espacio.espacio import Espacio
from src.app.domain.model.bodega.bodega import Bodega
from src.app.infrastructure.domain.event.in_memory.in_memory_event_store import InMemoryEventStore


def test_create_space_successfully_add_event():
    InMemoryEventStore().clear_all()
    bodega_test=Bodega("bodega-test-1")
    Espacio("esp-1",10,100,bodega_test.get_id())
    assert len(InMemoryEventStore().all_events_since(0))==2