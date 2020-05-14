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
    volume: float  # m3
    weight: float  # kg
    qty: float


@dataclass
class OrderLine(Product):
    reference: str

    @property
    def total_weight(self): return self.qty * self.weight

    @property
    def total_volume(self): return self.qty * self.volume


'''
max_weight in kg
max_vol in m3
availables in %
'''


class WhSpace:
    def __init__(self, reference: str, products: List[Product], max_vol: int, max_weigth: int):
        self.ref = reference
        self.products = products
        self.max_vol = max_vol
        self.max_weight = max_weigth

    @property
    def available_weight(self):
        total_weight = 0
        for product in self.products:
            total_weight = total_weight + (product.weight * product.qty)
        return self.max_weight - total_weight

    @property
    def available_vol(self):
        total_volume = 0
        for product in self.products:
            total_volume = total_volume + (product.volume * product.qty)
        return self.max_vol - total_volume

    def add(self, line: OrderLine):
        self.products.append(Product(sku=line.sku,
                                     description=line.description,
                                     qty=line.qty,
                                     weight=line.weight,
                                     volume=line.volume))

    def empty(self):
        self.products.clear()

    @property
    def prods_qty(self):
        total_prods = 0
        for product in self.products:
            total_prods = total_prods + product.qty
        return total_prods


class CantBeAllocated(Exception):
    pass


class NotEmpty(Exception):
    pass


def allocate(line: OrderLine, space: WhSpace):
    if line.total_volume > space.available_vol:
        raise CantBeAllocated(f'el volumen del sku {line.reference} excede el volumen disponible en el espacio')
    elif line.total_weight > space.available_weight:
        raise CantBeAllocated(f'el peso del sku {line.reference} excede el peso disponible en el espacio')
    else:
        space.add(line)


def deallocate(orderline, space: WhSpace):
    for product in space.products:
        if product.sku == orderline.sku:
            if product.qty == orderline.qty:
                space.products.remove(product)
            elif product.qty < orderline.qty:
                raise ValueError("El producto {orderline.sku} excede la"
                                 " cantidad disponible en el espacio")
            product.qty = product.qty - orderline.qty



class abstractWarehouse(ABC):

    def add(self, reference: str):
        return NotImplementedError("Metodo no Implementado")

    def get(self, reference: str):
        return NotImplementedError("Metodo no Implementado")

    def delete(self, reference: str):
        return NotImplementedError("Metodo no Implementado")

    def get_all(self):
        return NotImplementedError("Metodo no Implementado")


class FakeWarehouse(abstractWarehouse):

    def __init__(self, reference: str):
        self.ref = reference
        self.spaces = list()

    def add(self, reference: str):
        self.spaces.append(reference)

    def get(self, reference: str):
        for space in self.spaces:
            if reference == space.ref:
                return space

    def delete(self, reference: str):
        for space in self.spaces:
            if not space.products:
                self.spaces.remove(reference)
            else:
                raise NotEmpty(f"Espacio {space.ref} no esta vacio")

    def get_all(self):
        return self.spaces
