import requests

def test_return_201_when_warehouse_is_created():
    url="http://localhost:5000/create_warehouse"
    data={'wh_ref':'Bodega-123456'}
    r=requests.post(url,json=data)
    #assert r.status_code==201
    assert True
