from dataclasses import dataclass
import abc
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
class WarehouseCreated(Event):
    wh_id: str


@dataclass
class UserCreated(Event):
    event_id: str

class DummyEventsRaiser:

    def __init__(self):
        self.events = []

    def event_triggered(self, reference: str):
        self.events.append(WarehouseCreated(wh_id=reference))
