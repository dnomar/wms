from src.app.domain.model.Exeptions import CantBeAllocated, NotEmpty, NotAssignedSpaceException, EmptyWarehouseReference
from src.app.domain.model.OrderLine import OrderLine
from src.app.domain.model.Space import Space
from src.app.domain.model.Warehouse import Warehouse
from src.app.domain.model.Product import Product
from src.app.service_layer.service import allocate, deallocate
import pytest
from test.randoms import *
from test.unit.fakes.fake_warehouse_repository import FakeWarehouseRepository


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
    espacio1 = Space(reference=rnd_space_sku1, max_weigth=50, max_vol=1)
    espacio2 = Space(reference=rnd_space_sku2, max_weigth=50, max_vol=1)

    warehouse.add_space(espacio1)
    warehouse.add_space(espacio2)
    assert warehouse.list_allocated_spaces() == list([espacio1, espacio2])
    warehouse.delete_space(espacio2)
    assert warehouse.list_allocated_spaces() == list([espacio1])


def test_only_empty_space_could_be_unassigned():
    warehouse = Warehouse("Bodega 1")
    rnd_space_sku1 = random_space('o1')
    rnd_prod_sku = random_product('TP')
    espacio1 = Space(reference=rnd_space_sku1, max_vol=0.5, max_weigth=50)
    warehouse.add_space(espacio1)
    allocate(OrderLine(sku=rnd_prod_sku, description="TERRIBLE PROD", qty=13, volume_unit=0.01,
                       weight_unit=0.5, reference="OL-2"), warehouse.get_space(espacio1.ref))

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


def test_update_warehouse_name_in_repository():
    # Given
    fakeWhRep = FakeWarehouseRepository()
    warehouse1 = Warehouse('Bodega-1')
    space1 = Space("space-1", 5, 10)
    warehouse1.add_space(space1)
    order_line1 = OrderLine('1312-4', "producto de pruea", 1, 1, 2, "order line 1")
    allocate(order_line1, space1)
    fakeWhRep.add(warehouse1)
    assert fakeWhRep.get('Bodega-1').get_warehouse_ref() == 'Bodega-1'
    with pytest.raises(EmptyWarehouseReference):
        fakeWhRep.get('Bodega-1').change_warehouse_ref('')
    fakeWhRep.get('Bodega-1').change_warehouse_ref('Bodega-2')
    assert fakeWhRep.get('Bodega-2').get_space('space-1').get_product('1312-4').description == "producto de pruea"

def test_product_to_dict():
    data={ 
        "sku": "sku-001",
        "description": "articulo de prueba",
        "volume_unit": 1,
        "weight_unit": 0.1,
        "qty": 5
    }
    test_prod=Product("sku-001", "articulo de prueba", 1, 0.1, 5)
    assert data == test_prod.to_dict()

def test_space_to_dict():
    data= {
            "reference": "espacio-1",
            "max_volume": 100,
            "max_weight": 100,
            "productos": [
                {
                    "sku": "sku-001",
                    "description": "articulo de prueba",
                    "volume_unit": 1,
                    "weight_unit": 0.1,
                    "qty": 5
                },
                {
                    "sku": "sku-002",
                    "description": "articulo de prueba 2",
                    "volume_unit": 0.5,
                    "weight_unit": 0.05,
                    "qty": 10
                }
            ]
            }
    wh = Warehouse("Bodega-1")
    space = Space("espacio-1", 100, 100)
    wh.add_space(space)    
    orderline = OrderLine("sku-001", "articulo de prueba", 1, 0.1, 5, "o-l-1")
    orderline2 = OrderLine("sku-002", "articulo de prueba 2", 0.5, 0.05, 10, "o-l-2")
    allocate(orderline, wh.get_space('espacio-1'))
    allocate(orderline2, wh.get_space('espacio-1'))
    assert data == wh.list_allocated_spaces()[0].to_dict()



def test_get_warehouse_master():
    data = {
        "wh_ref": "Bodega-1",
        "allocated_spaces": [
            {
                "reference": "espacio-1",
                "max_volume": 100,
                "max_weight": 100,
                "productos": [
                    {
                        "sku": "sku-001",
                        "description": "articulo de prueba",
                        "volume_unit": 1,
                        "weight_unit": 0.1,
                        "qty": 5
                    },
                   {
                        "sku": "sku-002",
                        "description": "articulo de prueba 2",
                        "volume_unit": 0.5,
                        "weight_unit": 0.05,
                        "qty": 10
                    }
                ]
            }
        ]
    }
    wh = Warehouse("Bodega-1")
    space = Space("espacio-1", 100, 100)
    orderline = OrderLine("sku-001", "articulo de prueba", 1, 0.1, 5, "o-l-1")
    orderline2 = OrderLine("sku-002", "articulo de prueba 2", 0.5, 0.05, 10, "o-l-2")
    wh.add_space(space)
    allocate(orderline, wh.get_space('espacio-1'))
    allocate(orderline2, wh.get_space('espacio-1'))
    assert wh.to_dict()==data
