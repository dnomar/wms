import unittest
from src.wms.model import OrderLine, WhSpace, allocate, CantBeAllocated, Product
import pytest


class MyTestCase(unittest.TestCase):

    def test_orderline_volume(self):
        line = OrderLine('LINEA-001', '001-LENTES-002',
                       'LENTES TAQUILLEITOR', 10, 48, 5)
        assert line.volume == 48

    def test_product_can_not_be_allocated_if_line_exceed_space_volume(self):
        line = OrderLine('LINEA ABSTRACTA', '001-LENTES-002 ','LENTES TAQUILLEITOR', 10, 48, 0.501)
        space = WhSpace("A-25-2", 50, [], 0.5)

        with pytest.raises(CantBeAllocated, match=line.sku):
            allocate(line, space)

    def test_product_can_not_be_allocated_if_line_exceed_space_weight(self):
        line = OrderLine('LINEA ABSTRACTA', '001-LENTES-002 ','LENTES TAQUILLEITOR', 10, 50.1, 0.499)
        space = WhSpace("A-25-2", 50, [], 0.5)

        with pytest.raises(CantBeAllocated, match=line.sku):
            allocate(line, space)

    def test_product_can_be_allocated(self):
        line = OrderLine('LINEA ABSTRACTA', '001-LENTES-002','LENTES TAQUILLEITOR', 10, 0.499, 50.1)
        space = WhSpace("A-25-2", 50, [], 0.5)
        allocate(line,space)

        assert space.products[0].sku == line.sku
        assert space.products[0].qty == line.qty
        assert space.products[0].weight == line.weight
        assert space.products[0].volume == line.volume

    def test_product_can_not_be_allocated_if_space_doesnt_exist(self):
        self.assertFalse()
