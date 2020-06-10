from typing import Union

from src.wms.domain import events, commands
from src.wms.service_layer import handlers
from src.wms.service_layer.unit_of_work import AbstractUnitOfWork

Message = Union[commands.Command, events.Event]


def handle(message: Message, uow: AbstractUnitOfWork):
    queue = [message]
    while queue:
        msg = queue.pop(0)
        if isinstance(msg, commands.Command):
            for cmd in HANDLER_COMMANDS[type(msg)]:
                cmd(msg, uow)
        elif isinstance(msg, events.Event):
            for evnt in HANDLERS_EVENTS[type(msg)]:
                evnt(msg)
        else:
            raise NotEventOrCommandException(f'La instrucción {msg} no es un commando ni tampoco un evento')


HANDLERS_EVENTS = {
    events.WarehouseCreated: [handlers.send_warehouse_created_notification],
    events.UserCreated: [handlers.send_warehouse_created_notification],
}

HANDLER_COMMANDS = {
    commands.CreateWarehouse: [handlers.create_warehouse]
}

class NotEventOrCommandException(Exception):
    pass
