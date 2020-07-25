from src.app.domain.model.espacio.espacio import Espacio
from src.app.application.service.espacio.espacio_service import EspacioService
from src.app.infrastructure.domain.bodega.in_memory.in_memory_bodega_repository import InMemoryBodegaRepository


class MakeNewEspacioService:

    def __init__(self, name: str, max_volume: int, max_weigth: int, bodega_id:str, repo:EspacioService):
        self._name = name
        self._max_volume = max_volume
        self._max_weight = max_weigth
        self._bodega_id = bodega_id
        self._repo=repo
    
    def execute(self)->Espacio:
        self._repo.find_bodega_id_or_fail(self._bodega_id)
        nuevo_espacio = Espacio(self._name, self._max_volume, self._max_weight, self._bodega_id)
        #TODO: throw NewSpaceCreated event
        #TODO: Add NewSpaceToRepository
        return nuevo_espacio


        

