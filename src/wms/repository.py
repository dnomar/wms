import abc


from src.wms.model import NotEmpty


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

    def __init__(self, reference: str):
        self.ref = reference
        self.spaces = list()

    def add(self, reference: str):
        self.spaces.append(reference)

    def get(self, reference: str):
        for space in self.spaces:
            if reference == space.ref:
                return space

    def delete(self, reference: str):
        for space in self.spaces:
            if not space.products:
                self.spaces.remove(reference)
            else:
                raise NotEmpty(f"Espacio {space.ref} no esta vacio")

    def get_all(self):
        return self.spaces


class FakeOrderLineRepository(AbstractRepository):

    def __init__(self, session):
        self.session = session

    def add(self, reference: str):
        pass

    def get(self, reference: str):
        pass
