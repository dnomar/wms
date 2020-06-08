from src.wms.events import DummyEventsRaiser
from src.wms import messagebus, message
from test.fakemail import FakeMail


def test_dummy_class_raises_an_event():
    dummy = DummyEventsRaiser()
    dummy.event_triggered('Bodega-1')
    messagebus.handle(dummy.get_all_events())
    assert len(dummy.get_all_events()) == 1
    assert dummy.get_all_events()[0].event_name == 'WarehouseCreated'
    assert len(FakeMail().get_mailstack()) == 1
