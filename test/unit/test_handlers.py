import pytest
from src.wms.domain import commands, events
from src.wms.service_layer import messagebus
from src.wms.service_layer.messagebus import NotEventOrCommandException
from test.unit.fakes.fake_warehouse_unit_of_work import FakeWarehouseUnitOfWork
from test.unit.fakes.fakemail import FakeMail


def test_create_new_warehouse():
    uow = FakeWarehouseUnitOfWork()
    messagebus.handle(commands.CreateWarehouse("Bodega-1"), uow)
    assert len(uow.warehouses.get_all()) == 1
    assert len(uow.logger.get_all()) == 1
    assert uow.committed


def test_allocate_space_in_a_warehouse():
    uow = FakeWarehouseUnitOfWork()
    messagebus.handle(commands.CreateWarehouse("Bodega-1"), uow)
    messagebus.handle(commands.AllocateSpace("Bodega-1", "Espacio-1", 80, 1), uow)
    assert len(uow.warehouses.get("Bodega-1").list_allocated_spaces()) == 1


def test_no_command_exception():
    with pytest.raises(NotEventOrCommandException, match="not_command"):
        messagebus.handle("not_command", FakeWarehouseUnitOfWork())
