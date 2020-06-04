from src.wms import events
from src.wms import messagebus
import sys


def p_message_bus():
    messagebus.handle([events.WarehouseCreated])


if __name__ == "__main__":
    p_message_bus()
