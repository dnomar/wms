from src.app.domain.model.bodega.bodega import Bodega


class BodegaFactory:

    def __init__(self, name:str):
        self._name=name
    
    def execute(self)->Bodega:
        return Bodega(self._name)
