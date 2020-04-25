from src.wms.model import OrderLine, WhSpace, allocate, \
    CantBeAllocated, Product, FakeWarehouse, NotEmpty
import pytest
import uuid


def random_suffix():
    return uuid.uuid4().hex[:6]


def random_sku(name=''):
    return f'sku-{name}-{random_suffix()}'


def random_batchref(name=''):
    return f'batch-{name}-{random_suffix()}'


def random_orderid(name=''):
    return f'order-{name}-{random_suffix()}'


def random_space(name=''):
    return f'space-{name}-{random_suffix()}'


def test_orderline_volume():
    line = OrderLine('LINEA-001', '001-LENTES-002',
                     'LENTES TAQUILLEITOR', 10, 48, 5)
    assert line.volume == 48


def test_product_can_not_be_allocated_if_line_exceed_space_volume():
    line = OrderLine('LINEA ABSTRACTA', '001-LENTES-002 ', 'LENTES TAQUILLEITOR', 10, 48, 0.501)
    space = WhSpace("A-25-2", 50, [], 0.5)

    with pytest.raises(CantBeAllocated, match=line.sku):
        allocate(line, space)


def test_product_can_not_be_allocated_if_line_exceed_space_weight():
    line = OrderLine('LINEA ABSTRACTA', '001-LENTES-002 ', 'LENTES TAQUILLEITOR', 10, 50.1, 0.499)
    space = WhSpace("A-25-2", 50, [], 0.5)

    with pytest.raises(CantBeAllocated, match=line.sku):
        allocate(line, space)


def test_product_can_be_allocated():
    line = OrderLine('LINEA ABSTRACTA', '001-LENTES-002', 'LENTES TAQUILLEITOR', 10, 0.499, 50.1)
    space = WhSpace("A-25-2", 50, [], 0.5)
    allocate(line, space)
    assert space.products[0].sku == line.sku
    assert space.products[0].qty == line.qty
    assert space.products[0].weight == line.weight
    assert space.products[0].volume == line.volume


def test_space_can_be_asigned_to_a_warehouse():
    warehouse = FakeWarehouse("Bodega 1")
    rnd_space_sku = random_space('o1')
    espacio = WhSpace(rnd_space_sku, 50, [], 0.5)
    warehouse.add(espacio)
    assert warehouse.get(rnd_space_sku) == espacio


def test_space_can_be_unasigned_from_a_warehouse():
    warehouse = FakeWarehouse("Bodega 1")
    rnd_space_sku1 = random_space('o1')
    rnd_space_sku2 = random_space('o2')
    espacio1 = WhSpace(rnd_space_sku1, 50, [], 0.5)
    espacio2 = WhSpace(rnd_space_sku2, 50, [], 0.5)
    warehouse.add(espacio1)
    warehouse.add(espacio2)
    assert warehouse.get_all() == list([espacio1, espacio2])
    espacio2.empty()
    warehouse.delete(espacio2)
    assert warehouse.get_all() == list([espacio1])


def test_only_empty_space_could_be_unassigned():
    warehouse = FakeWarehouse("Bodega 1")
    rnd_space_sku1 = random_space('o1')
    espacio1 = WhSpace(rnd_space_sku1, 50, [], 0.5)
    warehouse.add(espacio1)

    with pytest.raises(NotEmpty, match=espacio1.ref):
        warehouse.delete(espacio1)


def test_product_deallocation():

    assert False




