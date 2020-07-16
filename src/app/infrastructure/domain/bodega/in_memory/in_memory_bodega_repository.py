from src.app.domain.model.bodega.bodega_repository import BodegaRepository
from src.app.domain.model.bodega.bodega import Bodega


class InMemoryBodegaRepository(BodegaRepository):

    def __init__(self):
        self._bodegas=set()

    def append(self, bodega:Bodega):
        self._bodegas.add(bodega)

    def find_by_id(self, bodega_id:str)->Bodega:
        return [x for x in self._bodegas if x.get_id()==bodega_id]
    
    def number_elements(self):
        print(len(self._bodegas))
        return len(self._bodegas)

    def clear_all(self):
        self._bodegas.clear()


