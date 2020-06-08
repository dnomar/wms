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


class Space:
    def __init__(self, reference: str, max_vol: int, max_weigth: int):
        self.ref = reference
        self._products = []  # List[Product]
        self.max_vol = max_vol
        self.max_weight = max_weigth
        self._assigned_to_warehouse = False

    def allocate(self, line: OrderLine):
        if not self.is_assigned():
            raise NotAssignedSpaceException(f" El espacio {self.ref} no esta asignado a ninguna bodega")
        self._products.append(Product(sku=line.sku, description=line.description, qty=line.qty,
                                      weight_unit=line.weight_unit, volume_unit=line.volume_unit))

    def remove_product(self, product: Product):
        self._products.remove(product)

    def get_product(self, sku: str):
        for prod in self._products:
            if prod.sku == sku:
                return prod

    def list_prod(self):
        return self._products

    def empty_space(self):
        self._products.clear()

    def space_assigned(self):
        self._assigned_to_warehouse = True

    def is_assigned(self):
        return self._assigned_to_warehouse

    @property
    def available_weight(self):
        total_weight = 0
        for product in self._products:
            total_weight = total_weight + (product.weight_unit * product.qty)
        return self.max_weight - total_weight

    @property
    def available_vol(self):
        total_volume = 0
        for product in self._products:
            total_volume = total_volume + (product.volume_unit * product.qty)
        return self.max_vol - total_volume

    @property
    def prods_qty(self):
        total_prods = 0
        for product in self._products:
            total_prods = total_prods + product.qty
        return total_prods


class Warehouse:

    def __init__(self, wh_reference: str):
        self.wh_ref = wh_reference
        self.spaces = []

    def add_space(self, space: Space):
        space.space_assigned()
        self.spaces.append(space)

    def get_space(self, space_reference: str):
        for space in self.spaces:
            if space_reference == space.ref:
                return space

    def delete_space(self, space_reference: str):
        for space in self.spaces:
            if not space.list_prod():
                self.spaces.remove(space_reference)
            else:
                raise NotEmpty(f"Espacio {space.ref} no esta vacio")

    def list_spaces(self):
        return self.spaces


class CantBeAllocated(Exception): pass


class NotEmpty(Exception): pass


class NotAssignedSpaceException(Exception): pass
