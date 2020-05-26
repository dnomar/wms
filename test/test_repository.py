from src.wms.repository import FakeOrderLineRepository
from src.wms.model import OrderLine


class FakeSession:

    def __init__(self):
        self._commited = False

    def commit(self):
        self._commited = True

    def rollback(self):
        pass


def test_repository_can_save_orderline():
    session = FakeSession()
    repo = FakeOrderLineRepository(session)
    order = OrderLine(sku="001-Lentes-001", description="LENTES PULENTOS", volume_unit=0.1,
                      weight_unit=10, reference="INGRE-01", qty=10)
    repo.add(order)
    assert session.commit()
    assert len(repo.get_all()) == 1
    assert repo.get("001-Lentes-001").description == order.description

