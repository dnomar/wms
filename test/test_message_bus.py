from src.wms import events
from src.wms import messagebus


def test_message_bus():
    messagebus.handle([events.WarehouseCreated])


if __name__=="__main__":
    test_message_bus()