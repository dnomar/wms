from src.wms.domain import events, commands
from src.wms.domain.model import Space, Warehouse
from src.wms.service_layer import unit_of_work
from test.unit.fakes.fake_warehouse_repository import FakeWarehouseRepository
from test.unit.fakes.fakemail import FakeMail


def send_warehouse_created_notification(event: events.WarehouseCreated):
    fkm = FakeMail()
    fkm.send("volivaresh@gmail.com", f"algo pal body {event.occurred_on}")


def create_warehouse(cmd: commands.CreateWarehouse, uow: unit_of_work.AbstractUnitOfWork):
    with uow:
        uow.warehouses.add(Warehouse(cmd.reference))
        uow.logger.add(events.WarehouseCreated(
            wh_name=cmd.reference
        ))
        uow.commit()


def allocate_space(cmd: commands.AllocateSpace, uow: unit_of_work.AbstractUnitOfWork):
    space = Space(cmd.space_reference, cmd.max_weight, cmd.max_vol)
    with uow:
        wh = uow.warehouses.get(cmd.warehouse_ref)
        wh.add_space(space)
        uow.logger.add(events.SpaceAllocated(
            space_ref=cmd.space_reference
        ))
