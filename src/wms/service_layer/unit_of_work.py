import abc
from src.wms.adapters import repository
from test.unit.fakes.fake_warehouse_repository import FakeWarehouseRepository


class AbstractUnitOfWork(abc.ABC):
    logger = repository.AbstractRepository

    def __exit__(self, *args):
        self.rollback()

    @abc.abstractmethod
    def commit(self):
        raise NotImplementedError

    @abc.abstractmethod
    def rollback(self):
        raise NotImplementedError


class AbstractWarehouseUnitOfWork(AbstractUnitOfWork):
    warehouse: FakeWarehouseRepository

    def __enter__(self):
        pass

    def __exit__(self, *args):
        self.rollback()