# SLI WMS INTENTO 5000000...
# #dimensiones en mm
# #peso en kg
from abc import ABC
from dataclasses import dataclass
from typing import List


@dataclass
class Product:
    sku: str
    description: str
    volume_unit: float  # m3
    weight_unit: float  # kg
    qty: float


@dataclass
class OrderLine(Product):
    reference: str


    @property
    def total_weight(self): return self.qty * self.weight_unit

    @property
    def total_volume(self): return self.qty * self.volume_unit


class WhSpace:
    def __init__(self, reference: str, max_vol: int, max_weigth: int):
        self.ref = reference
        self.products = [] #List[Product]
        self.max_vol = max_vol
        self.max_weight = max_weigth

    @property
    def available_weight(self):
        total_weight = 0
        for product in self.products:
            total_weight = total_weight + (product.weight_unit * product.qty)
        return self.max_weight - total_weight

    @property
    def available_vol(self):
        total_volume = 0
        for product in self.products:
            total_volume = total_volume + (product.volume_unit * product.qty)
        return self.max_vol - total_volume


    def add(self, line: OrderLine):
        self.products.append(Product(sku=line.sku,
                                     description=line.description,
                                     qty=line.qty,
                                     weight_unit=line.weight_unit,
                                     volume_unit=line.volume_unit))


    def empty(self):
        self.products.clear()

    @property
    def prods_qty(self):
        total_prods = 0
        for product in self.products:
            total_prods = total_prods + product.qty
        return total_prods


class Warehouse:

    def __init__(self, reference: str):
        self._reference: reference
        self.spaces: [] #List[WhSpace]

    def add(self, space: WhSpace):
        self.spaces.add(space)





class CantBeAllocated(Exception):
    pass


class NotEmpty(Exception):
    pass






