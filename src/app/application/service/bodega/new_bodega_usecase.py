from src.app.domain.model.bodega.bodega_repository import BodegaRepository
from src.app.application.service.bodega.bodega_request import BodegaRequest
from src.app.domain.model.bodega.bodega import Bodega

class NewBodegaUseCase:

    def __init__(self, repo:BodegaRepository):
        self.repo=repo
    

    def execute(self, request:BodegaRequest):
        new_bodega = Bodega(request.get_name())
        self.repo.append(new_bodega)

