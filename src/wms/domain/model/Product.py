from dataclasses import dataclass


@dataclass
class Product:
    sku: str
    description: str
    volume_unit: float  # m3
    weight_unit: float  # kg
    qty: float