from src.wms import events
from test.fakemail import FakeMail


def handle(event: events.Event):
    for evnt in event:
        for handler in HANDLERS[type(evnt)]:
            handler(evnt)


def send_warehouse_created_notification(event: events.WarehouseCreated):
    fkm = FakeMail()
    fkm.send("volivaresh@gmail.com", f"algo pal body {event.occurred_on}")


HANDLERS = {
    events.WarehouseCreated: [send_warehouse_created_notification],
    events.UserCreated: [send_warehouse_created_notification],
}
