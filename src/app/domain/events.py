from dataclasses import dataclass
import time
import datetime


@dataclass
class Event:

    @property
    def occurred_on(self):
        return datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M:%S %d-%m-%Y')

    @property
    def event_name(self):
        return type(self).__name__

@dataclass
class UserCreated(Event):
    event_id: str

@dataclass
class SpaceAllocated(Event):
    space_ref: str

@dataclass
class OrderLineAllocated(Event):
    order_line_ref:str
    space_ref:str
    warehouse_ref:str


