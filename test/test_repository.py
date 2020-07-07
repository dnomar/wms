from src.app.domain.model.OrderLine import OrderLine
from test.unit.fakes.fake_orderline_repository import FakeOrderLineRepository
from test.unit.fakes.fake_session import FakeSession


def test_repository_can_save_orderline():
    session = FakeSession()
    repo = FakeOrderLineRepository()
    order = OrderLine(sku="001-Lentes-001", description="LENTES PULENTOS", volume_unit=0.1,
                      weight_unit=10, reference="INGRE-01", qty=10)
    repo.add(order)
    assert session.commit()
    assert len(repo.get_all()) == 1
    assert repo.get("INGRE-01").description == order.description
