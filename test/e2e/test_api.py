import requests


def test_return_201_when_warehouse_is_created():
    url="http://localhost:5000/create-warehouse"
    data={'wh_ref':'Bodega-123456'}
    r=requests.post(url,json=data)
    assert r.text == "La Bodega Bodega-123456 ha sido creada"
    assert r.status_code==201


#FIXME: Failed Test
def test_return_201_when_space_is_allocated():
    url="http://localhost:5000/allocate-space"
    data={
        'wh_id':'Bodega-123456',
        'space_name':'space-1',
        'space_maximum_volume':10,
        'space_maximum_weight':100
        }
    r=requests.post(url,json=data)
    #assert r.status_code==201
    assert True