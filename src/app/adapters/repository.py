import abc


class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def add(self, reference: str):
        return NotImplementedError("Metodo no Implementado")

    @abc.abstractmethod
    def get_all(self):
        return NotImplementedError("Metodo no Implementado")



