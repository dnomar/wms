import abc

from src.wms.model import OrderLine, Warehouse


class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def add(self, reference: str):
        return NotImplementedError("Metodo no Implementado")

    @abc.abstractmethod
    def get(self, reference: str):
        return NotImplementedError("Metodo no Implementado")

    def delete(self, reference: str):
        return NotImplementedError("Metodo no Implementado")

    def get_all(self):
        return NotImplementedError("Metodo no Implementado")


class FakeWarehouseRepository(AbstractRepository):

    def __init__(self, reference:str):
        self.warehouses = []
        self.reference=reference

    def add(self, warehouse: Warehouse):
        self.warehouses.append(warehouse)

    def get(self, reference: str):
        for wh in self.warehouses:
            if reference == wh.ref:
                return wh

    def get_all(self):
        return self.warehouses


class FakeOrderLineRepository(AbstractRepository):

    def __init__(self):
        self.order_lines=[]

    def add(self, orderline: OrderLine):
        self.order_lines.append(orderline)

    def get(self, reference: str):
        for oline in self.order_lines:
            if reference == oline.reference:
                return oline

    def get_all(self):
        return self.order_lines

