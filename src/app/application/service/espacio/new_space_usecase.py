from src.app.application.service.espacio.allocate_espacio_request import AllocateEspacioRequest
from src.app.application.service.espacio.espacio_service import EspacioService
from src.app.domain.model.bodega.bodega_repository import BodegaRepository
from src.app.domain.model.espacio.espacio_repository import EspacioRepository
from src.app.domain.model.espacio.espacio import Espacio
from src.app.domain.model.shared.exceptions import NonExistingWarehouseException, SpaceAlreadyExistException
from src.app.application.service.espacio.espacio_dto import EspacioDTO

class NewSpaceUseCase:

    def __init__(self, bodega_repo: BodegaRepository, espacio_repo:EspacioRepository):
        self._bodega_repo = bodega_repo
        self._espacio_repo = espacio_repo
        self._espacio_service=EspacioService(self._bodega_repo, self._espacio_repo)


    def execute(self, request:AllocateEspacioRequest):
        wh_id=self._espacio_service.find_bodega(request.get_wh_id())
        print(f"Bodega ... {wh_id}")
        if not wh_id:
            raise NonExistingWarehouseException(f"La Bodega indicada {request.get_wh_id()} no existe")
        space_name=self._espacio_service.find_espacio(request.get_space_name())
        if space_name is not None:
            ##TODO: Consultar si nuestro modelo solo soportara 1 bodega
            raise SpaceAlreadyExistException  (f"El espacio {request.get_space_name()} indicado ya existe")
        new_espacio = Espacio(request.get_space_name(), request.get_max_volume(), request.get_max_weight(), request.get_wh_id())
        return EspacioDTO(new_espacio)

