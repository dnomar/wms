from src.app.domain.model.bodega.bodega_repository import BodegaRepository
from src.app.application.service.bodega.bodega_dto import BodegaDTO

class GetWarehouseIdUseCase:

    def __init__(self, repo: BodegaRepository):
        self._repo=repo

    def execute(self, warehousename:str):
        warehouse = self._repo.find_by_name(warehousename)
        return (BodegaDTO(warehouse).getId())