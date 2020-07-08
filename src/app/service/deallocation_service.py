import json
from src.app.domain.orderLine import OrderLine
from src.app.domain.exceptions import CantBeAllocated
from src.app.domain.space import Space
from src.app.domain.warehouse import Warehouse


def deallocate(line: OrderLine, space: Space):
    for product in space.list_prod():
        if product.sku == line.sku:
            if product.qty == line.qty:
                space.remove_product(product)
            elif product.qty < line.qty:
                raise ValueError(f'El producto {line.sku} excede la cantidad disponible en el espacio')
            product.qty = product.qty - line.qty


