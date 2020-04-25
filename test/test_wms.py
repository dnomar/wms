from src.wms.model import OrderLine, WhSpace, allocate, \
    CantBeAllocated, Product, FakeWarehouse, NotEmpty, deallocate
import pytest
import uuid


def random_suffix():
    return uuid.uuid4().hex[:6]


def random_sku(name=''):
    return f'sku-{name}-{random_suffix()}'


def random_product(name=''):
    return f'product-{name}-{random_suffix()}'


def random_orderid(name=''):
    return f'order-{name}-{random_suffix()}'


def random_space(name=''):
    return f'space-{name}-{random_suffix()}'


def test_orderline_volume():
    line = OrderLine( sku='001-LENTES-002',
                     description= 'LENTES TAQUILLEITOR',
                      qty=10, weight= 48, volume= 5,
                      reference='LINEA-001')
    assert line.volume == 5
    assert line.total_weight == 480
    assert line.total_volume == 50



def test_product_can_not_be_allocated_if_line_exceed_space_volume():
    line = OrderLine('001-LENTES-002 ', 'LENTES TAQUILLEITOR', 10, 48, 0.501, 'LINEA ABSTRACTA')
    space = WhSpace("A-25-2", 50, [], 0.5)

    with pytest.raises(CantBeAllocated, match=line.sku):
        allocate(line, space)


def test_product_can_not_be_allocated_if_line_exceed_space_weight():
    line = OrderLine('001-LENTES-002 ', 'LENTES TAQUILLEITOR', 10, 50.1, 0.499, 'LINEA ABSTRACTA')
    space = WhSpace("A-25-2", 50, [], 0.5)

    with pytest.raises(CantBeAllocated, match=line.sku):
        allocate(line, space)


def test_product_can_be_allocated():
    line = OrderLine(sku='001-LENTES-002', description='LENTES TAQUILLEITOR',
                     qty=10, volume=.499, weight=49.9, reference='LINEA ABSTRACTA')
    space = WhSpace(reference="A-25-2", products=[], max_vol=.5, max_weigth=50)
    allocate(line, space)
    assert space.products[0].sku == line.sku
    assert space.products[0].description == line.description
    assert space.products[0].weight == line.weight
    assert space.products[0].volume == line.volume


def test_space_can_be_asigned_to_a_warehouse():
    warehouse = FakeWarehouse("Bodega 1")
    rnd_space_sku = random_space('o1')
    espacio = WhSpace(reference=rnd_space_sku, max_weigth=50,
                      products=[], max_vol= 0.5)
    warehouse.add(espacio)
    assert warehouse.get(rnd_space_sku) == espacio


def test_empty_space_can_be_unasigned_from_a_warehouse():
    warehouse = FakeWarehouse("Bodega 1")
    rnd_space_sku1 = random_space('o1')
    rnd_space_sku2 = random_space('o2')
    espacio1 = WhSpace(reference=rnd_space_sku1, max_weigth=50,
                      products=[], max_vol=0.5)
    espacio2 = WhSpace(reference=rnd_space_sku2, max_weigth=50,
                      products=[], max_vol=0.5)
    warehouse.add(espacio1)
    warehouse.add(espacio2)
    assert warehouse.get_all() == list([espacio1, espacio2])
    warehouse.delete(espacio2)
    assert warehouse.get_all() == list([espacio1])


def test_only_empty_space_could_be_unassigned():
    warehouse = FakeWarehouse("Bodega 1")
    rnd_space_sku1 = random_space('o1')
    rnd_prod_sku = random_product('TP')
    espacio1 = WhSpace(rnd_space_sku1, [(rnd_prod_sku,"TERRIBLE PROD", 13, 0.01, 0.5)], 0.5, 50)
    warehouse.add(espacio1)

    with pytest.raises(NotEmpty, match=espacio1.ref):
        warehouse.delete(espacio1)


def test_product_deallocation():
    warehouse = FakeWarehouse("Bodega 1")
    rnd_space_sku1 = random_space('space')
    espacio1 = WhSpace(reference=rnd_space_sku1, max_weigth=50,
                      products=[], max_vol= 0.5)
    warehouse.add(espacio1)
    line = OrderLine(sku='001-LENTES-002', description='LENTES TAQUILLEITOR',
                     qty=10, volume=.499, weight=49.9, reference='LINEA ABSTRACTA')
    allocate(line, warehouse.get(rnd_space_sku1))
    assert warehouse.get(rnd_space_sku1).products[0].qty == line.qty
    unalloc_line = OrderLine(sku='001-LENTES-002', description='LENTES TAQUILLEITOR',
                     qty=5, volume=.499, weight=49.9, reference='LINEA ABSTRACTA')
    deallocate(unalloc_line, warehouse.get(rnd_space_sku1))
    assert warehouse.get(rnd_space_sku1).products[0].qty == 5





