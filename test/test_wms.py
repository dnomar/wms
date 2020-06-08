from src.wms.domain.model import OrderLine, Space, \
    CantBeAllocated, NotEmpty, NotAssignedSpaceException
from src.wms.service_layer.service import allocate, deallocate
from src.wms.adapters.repository import Warehouse
import pytest
from test.randoms import *


def test_calc_orderline_total_volume_and_total_weight():
    line = OrderLine(sku='001-LENTES-002',
                     description='LENTES TAQUILLEITOR',
                     qty=10, weight_unit=48, volume_unit=5,
                     reference='LINEA-001')
    assert line.total_weight == 480
    assert line.total_volume == 50


def test_product_can_not_be_allocated_if_line_exceed_space_volume():
    line = OrderLine(sku='001-LENTES-002 ', description='LENTES TAQUILLEITOR', qty=10,
                     weight_unit=48, volume_unit=0.501, reference='LINEA ABSTRACTA')
    space = Space(reference="A-25-2", max_weigth=50, max_vol=0.5)
    with pytest.raises(CantBeAllocated, match=line.sku):
        allocate(line, space)


def test_product_can_not_be_allocated_if_line_exceed_space_weight():
    line = OrderLine('001-LENTES-002 ', 'LENTES TAQUILLEITOR', 10, 50.1, 0.499, 'LINEA ABSTRACTA')
    space = Space(reference="A-25-2", max_weigth=50, max_vol=0.5)

    with pytest.raises(CantBeAllocated, match=line.sku):
        allocate(line, space)


def test_product_can_be_allocated_only_in_a_space_assigned_to_warehouse():
    wh = Warehouse("Bodega1")
    line = OrderLine(sku='001-LENTES-002', description='LENTES TAQUILLEITOR',
                     qty=10, volume_unit=0.499, weight_unit=49.9, reference='LINEA ABSTRACTA')
    space1 = Space(reference="A-25-2", max_vol=80000, max_weigth=5000000)
    wh.add_space(space1)
    allocate(line, wh.get_space("A-25-2"))
    assert wh.get_space("A-25-2").get_product('001-LENTES-002').sku == line.sku
    assert wh.get_space("A-25-2").get_product('001-LENTES-002').description == line.description
    assert wh.get_space("A-25-2").get_product('001-LENTES-002').weight_unit == line.weight_unit
    assert wh.get_space("A-25-2").get_product('001-LENTES-002').volume_unit == line.volume_unit

    space2 = Space(reference="A-25-3", max_vol=9900, max_weigth=5000)
    with pytest.raises(NotAssignedSpaceException, match=space2.ref):
        allocate(line, space2)


def test_space_can_be_assigned_to_a_warehouse():
    warehouse = Warehouse("Bodega 1")
    rnd_space_sku = random_space('o1')
    espacio = Space(reference=rnd_space_sku, max_weigth=50, max_vol=0.5)

    warehouse.add_space(espacio)
    assert warehouse.get_space(rnd_space_sku) == espacio


def test_only_empty_space_can_be_unassigned_from_a_warehouse():
    warehouse = Warehouse("Bodega 1")
    rnd_space_sku1 = random_space('o1')
    rnd_space_sku2 = random_space('o2')
    espacio1 = Space(reference=rnd_space_sku1, max_weigth=50, max_vol=0.5)
    espacio2 = Space(reference=rnd_space_sku2, max_weigth=50, max_vol=0.5)

    warehouse.add_space(espacio1)
    warehouse.add_space(espacio2)
    assert warehouse.list_spaces() == list([espacio1, espacio2])
    warehouse.delete_space(espacio2)
    assert warehouse.list_spaces() == list([espacio1])


def test_only_empty_space_could_be_unassigned():
    warehouse = Warehouse("Bodega 1")
    rnd_space_sku1 = random_space('o1')
    rnd_prod_sku = random_product('TP')
    espacio1 = Space(reference= rnd_space_sku1, max_vol= 0.5, max_weigth= 50)
    warehouse.add_space(espacio1)
    allocate(OrderLine(sku= rnd_prod_sku, description= "TERRIBLE PROD", qty= 13, volume_unit= 0.01,
                       weight_unit= 0.5, reference= "OL-2"), warehouse.get_space(espacio1.ref))

    with pytest.raises(NotEmpty, match=espacio1.ref):
        warehouse.delete_space(espacio1)


def test_product_can_deallocate():
    warehouse = Warehouse("Bodega 1")
    rnd_space_sku1 = random_space('space')
    espacio1 = Space(reference=rnd_space_sku1, max_weigth=500, max_vol=50)
    warehouse.add_space(espacio1)
    line1 = OrderLine(sku=random_sku("lentes"), description='LENTES TAQUILLEITOR', qty=4, volume_unit=.499,
                      weight_unit=49.9,
                      reference='LINEA ABSTRACTA 1')
    line2 = OrderLine(sku=random_sku("zapatos"), description='ZAPATOS TAQUILLEITOR', qty=5, volume_unit=.499,
                      weight_unit=49.9,
                      reference='LINEA ABSTRACTA 2')
    line3 = OrderLine(sku=random_sku("Ollas"), description='OLLAS TAQUILLEITOR', qty=1, volume_unit=.499,
                      weight_unit=49.9,
                      reference='LINEA ABSTRACTA 3')

    allocate(line1, warehouse.get_space(rnd_space_sku1))
    allocate(line2, warehouse.get_space(rnd_space_sku1))
    allocate(line3, warehouse.get_space(rnd_space_sku1))
    assert warehouse.get_space(rnd_space_sku1).prods_qty == line1.qty + line2.qty + line3.qty
    assert warehouse.get_space(rnd_space_sku1).available_weight == round(
        espacio1.max_weight - (line1.qty * line1.weight_unit) - \
        (line2.qty * line2.weight_unit) - (
                line3.qty * line3.weight_unit))
    assert warehouse.get_space(rnd_space_sku1).available_vol == espacio1.max_vol - (line1.qty * line1.volume_unit) - \
           (line2.qty * line2.volume_unit) - (line3.qty * line3.volume_unit)
    deallocate(line1, warehouse.get_space(rnd_space_sku1))
    assert warehouse.get_space(rnd_space_sku1).prods_qty == line2.qty + line3.qty

    deall_line = (OrderLine(line2.sku, line2.description, line2.volume_unit, line2.weight_unit, 2, "deall_line"))
    deallocate(deall_line, warehouse.get_space(rnd_space_sku1))
    assert warehouse.get_space(rnd_space_sku1).prods_qty == 4

    deall_line2 = (OrderLine(line2.sku, line2.description, line2.volume_unit, line2.weight_unit, 20, "deall_line"))
    with pytest.raises(ValueError, match=deall_line2.sku):
        deallocate(deall_line2, warehouse.get_space(rnd_space_sku1))
    assert warehouse.get_space(rnd_space_sku1).prods_qty == 4
