from src.app.adapters.repository import AbstractRepository
from src.app.domain.warehouse import Warehouse


class FakeWarehouseRepository(AbstractRepository):

    def __init__(self):
        self.warehouses = []

    def add(self, warehouse: Warehouse):
        self.warehouses.append(warehouse)

    def get(self, reference: str) -> Warehouse:
        for wh in self.warehouses:
            if reference == wh.get_warehouse_ref():
                return wh

    def get_all(self):
        return self.warehouses
