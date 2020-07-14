#ESTO ES UNA INTERFAZ 
from src.app.domain.model.bodega.bodega import Bodega
import abc

class BodegaRepository(abc.ABC):
    
    @abc.abstractmethod
    def find_by_id(self, bodega_id:str)->Bodega:
        raise NotImplementedError