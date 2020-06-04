from src.wms.events import DummyEventsRaiser
from src.wms import messagebus, message
from test.fakemail import FakeMail


def test_mail_messenger():
    fakemail = FakeMail()
    fakemail.send("pp@ppql.cl","este es el body de mi mensaje")
    fakemail.send("poringa@ppql.cl", "body mensaje 2")
    assert len(fakemail.get_mailstack()) == 2


def test_dummy_class_raises_an_event():
    dummy = DummyEventsRaiser()
    dummy.event_triggered('Bodega-1')
    messagebus.handle(dummy.events)
    assert len(dummy.events) == 1
    assert dummy.events[0].event_name == 'WarehouseCreated'
    assert len(FakeMail().get_mailstack()) == 1
