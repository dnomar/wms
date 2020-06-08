from src.wms.adapters.repository import FakeOrderLineRepository
from src.wms.domain.model import OrderLine


class FakeSession:

    def __init__(self):
        self._commited = False

    def commit(self):
        self._commited = True
        return self._commited

    def rollback(self):
        pass


def test_repository_can_save_orderline():
    session = FakeSession()
    repo = FakeOrderLineRepository()
    order = OrderLine(sku="001-Lentes-001", description="LENTES PULENTOS", volume_unit=0.1,
                      weight_unit=10, reference="INGRE-01", qty=10)
    repo.add(order)
    assert session.commit()
    assert len(repo.get_all()) == 1
    assert repo.get("INGRE-01").description == order.description
