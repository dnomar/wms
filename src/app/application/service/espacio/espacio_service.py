from src.app.domain.model.bodega.bodega import Bodega
from src.app.domain.model.bodega.bodega_repository import BodegaRepository
from src.app.domain.model.espacio.espacio import Espacio 
from src.app.domain.model.espacio.espacio_repository import EspacioRepository
from src.app.domain.exceptions import NonExistingWarehouseException

class EspacioService:

    def find_bodega_id_or_fail(self, bodega_id:str)->Bodega:
        pass

    def find_espacio_or_fail(self, espacio_id:str)->Espacio:
        pass


