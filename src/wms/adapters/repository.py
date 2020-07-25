import abc
from src.wms import model


class AbstractWarehouseRepository(abc.ABC):

    @abc.abstractmethod
    def add(self, warehouse: model.Warehouse):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, reference: str) -> model.Warehouse:
        raise NotImplementedError


class SqlAlchemyWarehouseRepository(AbstractWarehouseRepository):

    def __init__(self, session):
        self.session = session

    def add(self, warehouse: model.Warehouse):
        self.session.add(warehouse)

    def get(self, reference: str):
        return self.session.query(model.Warehouse).filter_by(reference=reference).first()
