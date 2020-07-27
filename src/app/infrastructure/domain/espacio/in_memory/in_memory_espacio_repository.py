from src.app.domain.model.espacio.espacio import Espacio
from src.app.domain.model.espacio.espacio_repository import EspacioRepository


class InMemoryEspacioRepository(EspacioRepository):

    def __init__(self):
        self._espacio=set()

    def append(self, espacio:Espacio):
        self._espacio.add(espacio)

    def find_by_id(self, espacio_id:str)->Espacio:
        for x in self._espacio:
            if x.get_id()==espacio_id:
                return x
        
    def find_by_name(self, espacio_name:str)->Espacio:
        for x in self._espacio:
            if x.get_name()==espacio_name:
                return x
    
    def number_elements(self):
        print(f"Number of elements ... {len(self._espacio)}")
        return len(self._espacio)

    def clear_all(self):
        self._espacio.clear()


