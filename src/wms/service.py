from src.wms.model import OrderLine, CantBeAllocated, WhSpace


def allocate(line: OrderLine, space: WhSpace):
    if line.total_volume > space.available_vol:
        raise CantBeAllocated(f'el volumen del sku {line.sku} excede el volumen disponible en el espacio')
    elif line.total_weight > space.available_weight:
        raise CantBeAllocated(f'el peso del sku {line.sku} excede el peso disponible en el espacio')
    else:
        space.add(line)


def deallocate(line: OrderLine, space: WhSpace):
    for product in space.products:
        if product.sku == line.sku:
            if product.qty == line.qty:
                space.products.remove(product)
            elif product.qty < line.qty:
                raise ValueError(f'El producto {line.sku} excede la cantidad disponible en el espacio')
            product.qty = product.qty - line.qty