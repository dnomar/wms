from src.app.infrastructure.domain.event.in_memory.in_memory_event_store import InMemoryEventStore
from src.app.domain.model.bodega.bodega import Bodega

def test_make_a_new_warehouse_trows_WarehouseCreatedEvent():
    bod1=Bodega("bodega-generica")
    assert len(InMemoryEventStore().all_events_since(0)) == 1