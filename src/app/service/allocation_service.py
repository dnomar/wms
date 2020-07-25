import json
from src.app.domain.orderline import OrderLine
from src.app.domain.exceptions import CantBeAllocated
from src.app.domain.space import Space
from src.app.domain.model.warehouse import Warehouse


def allocate(line: OrderLine, space: Space):
    if line.total_volume > space.available_vol:
        raise CantBeAllocated(f'el volumen del sku {line.sku} excede el volumen disponible en el espacio')
    elif line.total_weight > space.available_weight:
        raise CantBeAllocated(f'el peso del sku {line.sku} excede el peso disponible en el espacio')
    else:
        space.allocate(line)
