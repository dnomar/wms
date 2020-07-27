from src.app.domain.model.bodega.bodega import Bodega
from src.app.infrastructure.domain.event.in_memory.in_memory_event_store import InMemoryEventStore

def test_two_bodega_ids_should_be_different():
    bodega1=Bodega("Bodega-1")
    bodega2=Bodega("Bodega-2")
    assert bodega1.get_id() is not bodega2.get_id()

def test_retrieving_bodega_name():
    name = "Bodega-X"
    bodega1 = Bodega(name)
    assert bodega1.get_name() == name

def test_new_bodega_add_event():
    InMemoryEventStore().clear_all()
    Bodega("bodega-1")
    Bodega("bodega-2")
    Bodega("bodega-3")
    assert len(InMemoryEventStore().all_events_since(0))==3