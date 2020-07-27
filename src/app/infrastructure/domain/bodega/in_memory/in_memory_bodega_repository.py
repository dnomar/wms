from src.app.domain.model.bodega.bodega_repository import BodegaRepository
from src.app.domain.model.bodega.bodega import Bodega

class InMemoryBodegaRepository(BodegaRepository):
    _instance = None
 
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls, *args, **kwargs)
            cls._instance._bodegas=set()
        return cls._instance

    def append(self, bodega:Bodega):
        self._bodegas.add(bodega)

    def find_by_id(self, bodega_id:str)->Bodega:
        for x in self._bodegas:
            if x.get_id() == bodega_id:
                return x
    
    def find_by_name(self, bodega_name:str)->Bodega:
        print(f"Entramos a FbN...{bodega_name} - elementos en el repo ... {self.number_elements()}")
        for x in self._bodegas:
            print(f"Bodega en FbN {x.get_name()}")
            if x.get_name() == bodega_name:
                return x
    
    def number_elements(self):
        return len(self._bodegas)

    def clear_all(self):
        self._bodegas.clear()


