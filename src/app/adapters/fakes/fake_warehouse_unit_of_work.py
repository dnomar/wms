from src.app.adapters import repository
from src.app.service.unit_of_work import AbstractWarehouseUnitOfWork
from src.app.adapters.fakes.fake_loggin_repository import FakeLogginRepository
from src.app.adapters.fakes.fake_warehouse_repository import FakeWarehouseRepository


class FakeWarehouseUnitOfWork(AbstractWarehouseUnitOfWork):

    def __init__(self):
        self.warehouses = FakeWarehouseRepository()
        self.logger = FakeLogginRepository()
        self.committed = False

    def commit(self):
        self.committed = True

    def rollback(self):
        pass
