from dataclasses import dataclass


@dataclass
class Product:
    sku: str
    description: str
    volume_unit: float  # m3
    weight_unit: float  # kg
    qty: float

    def to_dict(self):
        data = {
            "sku": self.sku,
            "description": self.description,
            "volume_unit": self.volume_unit,
            "weight_unit": self.weight_unit,
            "qty": self.qty
        }
        return data
