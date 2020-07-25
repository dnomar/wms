import pytest
from src.app.domain import commands
from src.app.service import messagebus
from src.app.service.messagebus import NotEventOrCommandException
from src.app.service.unit_of_work import FakeWarehouseUnitOfWork
from src.app.domain.exceptions import WrongSpaceException
from src.app.domain.model.bodega.bodega import Bodega


""" def test_allocate_product_in_a_warehouse_space():
    uow = FakeWarehouseUnitOfWork()
    Bodega("Bodega-1")
    messagebus.handle(commands.AllocateSpace("Bodega-1", "Espacio-1", 80, 1), uow)
    messagebus.handle(commands.AllocateProduct("Espacio-1", "prod-001", "FASHION GLASSES", 0.5, 500, 3, "ol-001",
                                               "Bodega-1"), uow)
    assert len(uow.warehouses.get("Bodega-1").list_allocated_spaces()[0].list_prod()) == 1


def test_no_command_exception():
    with pytest.raises(NotEventOrCommandException, match="not_command"):
        messagebus.handle("not_command", FakeWarehouseUnitOfWork()) """



