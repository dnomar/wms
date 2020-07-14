import uuid
import pytest
from src.app.domain.exceptions import NonExistingWarehouseException
from src.app.domain.model.espacio.espacio import Espacio
from src.app.application.service.espacio.make_new_espacio import MakeNewEspacioService
from src.app.infrastructure.application.service.in_memory.in_memory_espacio_service import InMemoryEspacioService


def test_make_a_new_space_with_non_existing_warehouse_throws_an_non_existing_warehouse_exception():
    random_uuid=str(uuid.uuid4())
    with pytest.raises(NonExistingWarehouseException):
        MakeNewEspacioService("espacio-1",10,20,random_uuid,InMemoryEspacioService()).execute()
        

