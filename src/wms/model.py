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
    qty: int
    weight: float #kg
    volume: float #m3


@dataclass
class OrderLine(Product):
    reference: str


'''
max_weight in kg
max_vol in m3
availables in %
'''


class WhSpace:
    def __init__(self, reference: str, max_weigth: int, products: List[Product], max_vol: int):
        self.ref = reference
        self.max_weight = max_weigth
        self.products = products
        self.max_vol = max_vol

    @property
    def available_weight(self):
        return 50

    @property
    def available_vol(self):
        return 0.5

    def add(self, line: OrderLine):
        self.products.append(Product(line.sku, line.description, line.qty, line.weight, line.volume))


class CantBeAllocated(Exception):
    pass


def allocate(line: OrderLine, space: WhSpace):
    if line.volume > space.available_vol:
        raise CantBeAllocated(f'el volumen del sku {line.sku} excede el volumen disponible en el espacio')
    elif line.weight > space.available_weight:
        raise CantBeAllocated(f'el peso del sku {line.sku} excede el peso disponible en el espacio')
    else:
        space.add(line)


def deallocate(orderline, space: WhSpace):
    pass


class abstractWarehouse(ABC):

    def add(self, reference: str):
        return NotImplementedError("Metodo no Implementado")

    def get(self, reference: str):
        return NotImplementedError("Metodo no Implementado")

    def delete(self, reference: str):
        return NotImplementedError("Metodo no Implementado")

    def get_all(self):
        return NotImplementedError("Metodo no Implementado")
