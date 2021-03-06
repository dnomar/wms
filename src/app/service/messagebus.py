from typing import Union
from src.app.domain import events, commands
from src.app.service import handlers
from src.app.service.unit_of_work import AbstractUnitOfWork

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
    commands.CreateWarehouse: [handlers.create_warehouse],
    commands.AllocateSpace: [handlers.allocate_space],
    commands.AllocateProduct: [handlers.allocate_product]
}

class NotEventOrCommandException(Exception):
    pass
