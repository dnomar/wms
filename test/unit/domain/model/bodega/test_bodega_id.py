from src.app.domain.model.bodega.bodega import Bodega

def test_two_bodega_ids_should_be_different():
    bodega1=Bodega("Bodega-1")
    bodega2=Bodega("Bodega-2")

    assert bodega1.get_id() is not bodega2.get_id()

def test_retrieving_bodega_name():
    name = "Bodega-X"
    bodega1 = Bodega(name)
    assert bodega1.get_name() == name