import abc
from src.app.domain.model.espacio.espacio import Espacio
class EspacioRepository(abc.ABC):

    @abc.abstractmethod
    def append(self, espacio:Espacio):
        raise NotImplementedError
    
    @abc.abstractmethod
    def find_by_id(self, espacio_id:str)->Espacio:
        raise NotImplementedError

    @abc.abstractmethod
    def find_by_name(self, espacio_name:str)->Espacio:
        raise NotImplementedError

    @abc.abstractmethod
    def number_elements(self):
        raise NotImplementedError