from dataclasses import dataclass
import datetime, time


class Command:
    pass


@dataclass
class CreateWarehouse(Command):
    reference: str


@dataclass
class AllocateSpace(Command):
    warehouse_ref: str
    space_reference: str
    max_weight: float
    max_vol: float





