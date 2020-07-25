from src.app.domain import events, commands
from src.app.domain.orderline import OrderLine
from src.app.domain.space import Space
from src.app.domain.model.warehouse import Warehouse
from src.app.service import unit_of_work
from src.app.adapters.fakes.fakemail import FakeMail
from src.app.domain.model.bodega.bodega_created import BodegaCreated


def send_warehouse_created_notification(event: BodegaCreated):
    fkm = FakeMail()
    fkm.send("volivaresh@gmail.com", f"algo pal body {event.occurred_on}")

def create_warehouse(cmd: commands.CreateWarehouse, uow: unit_of_work.AbstractUnitOfWork):
    with uow:
        uow.warehouses.add(Warehouse(cmd.reference))
        uow.logger.add(BodegaCreated(
            wh_name=cmd.reference
        ))
        uow.commit()

def persist_warehouse(cmd: commands.CreateWarehouse, uow: unit_of_work.AbstractUnitOfWork):
    pass

def allocate_space(cmd: commands.AllocateSpace, uow: unit_of_work.AbstractUnitOfWork):
    space = Space(cmd.space_reference, cmd.max_weight, cmd.max_vol)
    with uow:
        wh = uow.warehouses.get(cmd.warehouse_ref)
        wh.add_space(space)
        uow.logger.add(events.SpaceAllocated(
            space_ref=cmd.space_reference
        ))

def allocate_product(cmd: commands.AllocateProduct, uow: unit_of_work.AbstractUnitOfWork):
    order_line = OrderLine(
        sku=cmd.prod_sku,
        description=cmd.prod_desc,
        volume_unit= cmd.unit_volume,
        weight_unit=cmd.unit_weight,
        qty=cmd.qty,
        reference=cmd.ord_line_ref
    )
    uow.warehouses.get(cmd.warehouse_ref).get_space(cmd.space_ref).allocate(order_line)
    uow.logger.add(events.OrderLineAllocated(
        order_line_ref=cmd.ord_line_ref,
        space_ref=cmd.space_ref,
        warehouse_ref=cmd.warehouse_ref
    ))