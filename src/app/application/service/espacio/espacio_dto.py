from src.app.domain.model.espacio.espacio import Espacio

class EspacioDTO:

    def __init__(self, espacio:Espacio):
        self._espacio=espacio
    
    def name(self):
        return self._espacio.get_name()
