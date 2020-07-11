import abc
from src.app.adapters import repository, file_exporter
from src.app.adapters.fakes.fake_warehouse_repository import FakeWarehouseRepository
from src.app.adapters.repository import AbstractRepository


class AbstractUnitOfWork(abc.ABC):
    repo = repository.AbstractRepository

    def __exit__(self, *args):
        self.rollback()

    def __enter__(self):
        return self

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


class AbstractExportUnitOfWork(abc.ABC):

    @abc.abstractmethod
    def write(self, content: str):
        pass


class TxtExportUnitOfWork(AbstractExportUnitOfWork):

    def __init__(self, path_to_file: str, access_mode: str):
        self.path = path_to_file
        self.access_mode = access_mode

    def __enter__(self):
        self.file = open(self.path, self.access_mode)

    def write(self, content):
        self.file.write(content)

    def __exit__(self, *args):
        self.file.close()


class FakeWarehouseUnitOfWork(AbstractUnitOfWork):

    def __enter__(self):
        self.repo=FakeWarehouseRepository()
        return super().__enter__()
        
    def __exit__(self, *args):
        pass

    def commit(self):
        pass

    def rollback(self):
        pass