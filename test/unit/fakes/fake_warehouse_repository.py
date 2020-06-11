from src.wms.adapters.repository import AbstractRepository
from src.wms.domain.model import Warehouse


class FakeWarehouseRepository(AbstractRepository):

    def __init__(self):
        self.warehouses = []

    def add(self, warehouse: Warehouse):
        self.warehouses.append(warehouse)

    def get(self, reference: str):
        for wh in self.warehouses:
            if reference == wh.wh_ref:
                return wh

    def get_all(self):
        return self.warehouses

