import sys
sys.path.append(r"C:\Users\vlonc_000\Documents\08 code\wms")
from src.app.infrastructure.domain.bodega.in_memory.in_memory_bodega_repository import InMemoryBodegaRepository
from src.app.domain.model.bodega.bodega import Bodega

import requests

def test_return_201_when_warehouse_is_created():
    bodega_repo=InMemoryBodegaRepository()
    bodega_repo.clear_all()
    url="http://localhost:5000/create-warehouse"
    data={'wh_ref':'Bodega-123456'}
    r=requests.post(url,json=data)
    assert r.text == "La Bodega Bodega-123456 ha sido creada"
    assert r.status_code==201

#TODO: HACER LOS NOMBRES DE BODEGA RANDOMS
def test_return_201_when_space_is_allocated():
    url1="http://localhost:5000/create-warehouse"
    r=requests.post(url1, json={'wh_ref':'Bodega-123leee'}) 
    
    url2=f"http://localhost:5000/warehouse-id/Bodega-123leee"
    r=requests.get(url2)
    warehouse_id=r.text

    url3="http://localhost:5000/allocate-space"
    data={
        'space_name':'space-1',
        'space_maximum_volume':10,
        'space_maximum_weight':100
        }
    data['wh_id']=warehouse_id
    r=requests.post(url3,json=data)
    assert r.status_code==201

def test_return_warehouse_id_by_name():
    url="http://localhost:5000/create-warehouse"
    data={'wh_ref':'Bodega-123456'}
    r=requests.post(url,json=data)
    url2=f"http://localhost:5000/warehouse-id/{data['wh_ref']}"
    r=requests.get(url2)
    print(f"El ID de la bodega es {r.text}")
    assert r.status_code == 200
    assert r.text is not None  
