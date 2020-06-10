import pytest
from src.wms.domain import commands, events
from src.wms.service_layer import messagebus
from src.wms.service_layer.messagebus import NotEventOrCommandException
from test.unit.fakes.fake_warehouse_repository import FakeWarehouseRepository
from test.unit.fakes.fake_warehouse_unit_of_work import FakeWarehouseUnitOfWork
from test.unit.fakes.fakemail import FakeMail


def test_create_new_warehouse():
    uow = FakeWarehouseUnitOfWork()
    messagebus.handle(commands.CreateWarehouse("Bodega-1"), uow)
    assert len(uow.warehouses.get_all()) == 1
    assert len(uow.logger.get_all()) == 1
    assert uow.committed


def test_no_command_exception():
    with pytest.raises(NotEventOrCommandException, match="not_command"):
        messagebus.handle("not_command")


def test_warehouse_created_event():
    messagebus.handle(events.WarehouseCreated("Bodega-1"))
    assert len(FakeMail().get_mailstack()) == 1
