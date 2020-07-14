from src.app.domain.model.bodega.bodega import Bodega
from src.app.infrastructure.domain.bodega.in_memory.in_memory_bodega_repository import InMemoryBodegaRepository
from src.app.domain.model.espacio.espacio import Espacio 
from src.app.domain.model.espacio.espacio_repository import EspacioRepository
from src.app.domain.exceptions import NonExistingWarehouseException

class InMemoryEspacioService:
    
    def __init__(self):
        self._bodega_repo=InMemoryBodegaRepository()

    def find_bodega_id_or_fail(self, bodega_id:str)->Bodega:
        tempo_bodega=self._bodega_repo.find_by_id(bodega_id)
        if not tempo_bodega:
            raise NonExistingWarehouseException
        return tempo_bodega

    def find_espacio_or_fail(self, espacio_id:str)->Espacio:
        pass