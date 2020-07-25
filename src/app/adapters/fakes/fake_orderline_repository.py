from src.app.adapters.repository import AbstractRepository
from src.app.domain.orderline import OrderLine


class FakeOrderLineRepository(AbstractRepository):

    def __init__(self):
        self.order_lines = []

    def add(self, orderline: OrderLine):
        self.order_lines.append(orderline)

    def get(self, reference: str):
        for oline in self.order_lines:
            if reference == oline.reference:
                return oline

    def get_all(self):
        return self.order_lines