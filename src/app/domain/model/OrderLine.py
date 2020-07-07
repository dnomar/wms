from dataclasses import dataclass
from src.app.domain.model.Product import Product


@dataclass
class OrderLine(Product):
    reference: str

    @property
    def total_weight(self): return self.qty * self.weight_unit

    @property
    def total_volume(self): return self.qty * self.volume_unit
