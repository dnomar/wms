from flask import Flask, jsonify, request, Response
from src.app.application.service.espacio.new_space_usecase import NewSpaceUseCase
from src.app.application.service.espacio.allocate_espacio_request import AllocateEspacioRequest
from src.app.application.service.bodega.new_bodega_usecase import NewBodegaUseCase
from src.app.infrastructure.domain.bodega.in_memory.in_memory_bodega_repository import InMemoryBodegaRepository
from src.app.application.service.bodega.bodega_request import BodegaRequest
from src.app.infrastructure.domain.espacio.in_memory.in_memory_espacio_repository import InMemoryEspacioRepository
from src.app.application.service.get_warehouse_id_by_name_usecase import GetWarehouseIdUseCase

app = Flask(__name__)


@app.route("/create-warehouse", methods=['POST'])
def create_warehouse():
    wh_ref = request.json['wh_ref']
    created_warehouse=NewBodegaUseCase(InMemoryBodegaRepository()).execute(BodegaRequest(wh_ref))
    return f"La Bodega {created_warehouse.name()} ha sido creada", 201


@app.route("/allocate-space", methods=['POST'])
def allocate_space():
    warehouse_id = request.json['wh_id']
    space_name = request.json['space_name']
    space_maximum_volume = request.json['space_maximum_volume']
    space_maximum_weight = request.json['space_maximum_weight']
    allocate_space_rqst=AllocateEspacioRequest(warehouse_id, space_name, space_maximum_volume, space_maximum_weight)
    allocated_space=NewSpaceUseCase(InMemoryBodegaRepository(), InMemoryEspacioRepository()).execute(allocate_space_rqst)
    return "OK", 201

@app.route("/warehouse-id/<warehousename>", methods=['GET'])
def get_warehouse_id_by_name(warehousename):
    warehouse_id=GetWarehouseIdUseCase(InMemoryBodegaRepository()).execute(warehousename)
    if warehouse_id is None: return 404
    return warehouse_id, 200

@app.route("/", methods=['GET'])
def get_version():
    data={
        "Title":"Symplex WMS",
        "License":"SLI Standard License",
        "Version":"1.0.0-Beta"
    }
    return jsonify(data), 200

if __name__=="__main__":
   app.run(
       host="0.0.0.0",
       port=5000,
       debug=True
   )