from src.wms.model import OrderLine, CantBeAllocated, Space, Warehouse
from src.wms import config
from src.wms.adapters.repository import SqlAlchemyWarehouseRepository


def create_warehouse(reference: str):
    session = config.postgres_session_factory()
    rp = SqlAlchemyWarehouseRepository(session)
    rp.add(Warehouse(wh_reference=reference))
    session.commit()


def allocate(line: OrderLine, space: Space):
    if line.total_volume > space.available_vol:
        raise CantBeAllocated(f'el volumen del sku {line.sku} excede el volumen disponible en el espacio')
    elif line.total_weight > space.available_weight:
        raise CantBeAllocated(f'el peso del sku {line.sku} excede el peso disponible en el espacio')
    else:
        space.allocate(line)


def deallocate(line: OrderLine, space: Space):
    for product in space.list_prod():
        if product.sku == line.sku:
            if product.qty == line.qty:
                space.remove_product(product)
            elif product.qty < line.qty:
                raise ValueError(f'El producto {line.sku} excede la cantidad disponible en el espacio')
            product.qty = product.qty - line.qty


if __name__ == "__main__":
    create_warehouse("test_warehouse")
