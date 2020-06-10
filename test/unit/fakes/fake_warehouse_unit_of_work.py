from src.wms.adapters import repository
from src.wms.service_layer.unit_of_work import AbstractWarehouseUnitOfWork
from test.unit.fakes.fake_loggin_repository import FakeLogginRepository
from test.unit.fakes.fake_warehouse_repository import FakeWarehouseRepository


class FakeWarehouseUnitOfWork(AbstractWarehouseUnitOfWork):

    def __init__(self):
        self.warehouses = FakeWarehouseRepository()
        self.logger = FakeLogginRepository()
        self.committed = False

    def commit(self):
        self.committed = True

    def rollback(self):
        pass
