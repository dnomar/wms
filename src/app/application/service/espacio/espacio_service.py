from src.app.domain.model.bodega.bodega import Bodega
from src.app.domain.model.bodega.bodega_repository import BodegaRepository
from src.app.domain.model.espacio.espacio import Espacio 
from src.app.domain.model.espacio.espacio_repository import EspacioRepository
from src.app.domain.exceptions import NonExistingWarehouseException


class EspacioService:

    def __init__(self, bod_repo:BodegaRepository, espacio_repo:EspacioRepository):
        self._bod_repo = bod_repo
        self._espacio_repo = espacio_repo

    def find_bodega_by_id(self, bodega_id:str)->Bodega:
        return self._bod_repo.find_by_id(bodega_id)

    def find_espacio_by_name(self, espacio_name:str)->Espacio:
        return self._espacio_repo.find_by_name(espacio_name)

