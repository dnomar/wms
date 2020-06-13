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


@dataclass
class AllocateProduct(Command):
    space_ref: str
    prod_sku: str
    prod_desc: str
    unit_volume: int
    unit_weight: int
    qty: int
    ord_line_ref: str
    warehouse_ref:str




