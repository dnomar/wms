from src.wms.model import OrderLine, CantBeAllocated, Space


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