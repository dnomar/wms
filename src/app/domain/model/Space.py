from src.app.domain.model.Exeptions import NotAssignedSpaceException
from src.app.domain.model.OrderLine import OrderLine
from src.app.domain.model.Product import Product
import json


class Space:
    def __init__(self, reference: str, max_vol: int, max_weigth: int):
        self.ref = reference
        self.max_vol = max_vol
        self.max_weight = max_weigth
        self._assigned_to_warehouse = False
        self._products = []  # List[Product]

    def allocate(self, line: OrderLine):
        if not self.is_assigned():
            raise NotAssignedSpaceException(f" El espacio {self.ref} no esta asignado a ninguna bodega")
        self._products.append(Product(sku=line.sku, description=line.description, qty=line.qty,
                                      weight_unit=line.weight_unit, volume_unit=line.volume_unit))

    def remove_product(self, product: Product):
        self._products.remove(product)

    def get_product(self, sku: str) -> Product:
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

    def product2dict(self, prod_list:[])->[]:
        prod_dict=[]
        for x in prod_list:
            prod_dict.append(x.to_dict())
        return prod_dict               
    
    def to_dict(self)->dict:
        data = {
            "reference": self.ref,
            "max_volume": self.max_vol,
            "max_weight": self.max_weight,
            "productos": self.product2dict(self._products)
        }
        return data


