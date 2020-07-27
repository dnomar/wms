from src.app.domain.model.bodega.bodega import Bodega

class BodegaDTO:

    def __init__(self, bodega:Bodega):
        self._bodega=bodega
    
    def name(self):
        return self._bodega.get_name()

    def getId(self):
        return self._bodega.get_id()
