import sys
sys.path.append(r"C:\Users\van-gerald.olivares\Documents\08 Code\wms")
from flask import Flask, jsonify, request, Response
from src.app.application.service.espacio.new_space_usecase import NewSpaceUseCase
from src.app.application.service.espacio.allocate_space_request import AllocateSpaceRequest

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
    allocated_space=NewSpaceUseCase().execute(AllocateSpaceRequest(warehouse_id, space_name, space_maximum_volume, space_maximum_weight)  )
    return f"El espacio {allocated_space.space_name()} ha sido asignado a la bodega {allocated_space.wh_name()}", 201

""" @app.route("/hello_world", methods=['GET'])
def allocate_endpoint():
    return jsonify({"message": "hello world"}), 200


@app.route("/create_warehouse", methods=['POST'])
def create_warehouse():
    wh_ref = request.json['wh_ref']
    NewBodegaUseCase(InMemoryBodegaRepository()).execute(BodegaRequest(wh_ref))
    return 'OK', 201

@app.route("/get_wh_master", methods=['POST'])
def get_warehouse_master():
    pass """

@app.route("/", methods=['GET'])
def get_version():
    data={
        "Title":"Symplex WMS",
        "License":"SLI Standard License",
        "Version":"1.0.0-Beta"
    }
    return jsonify(data), 200

if __name__=="__main__":
<<<<<<< HEAD
   app.run(
       host="0.0.0.0",
       port=5000,
       debug=True
   )
=======
    app.run(host="0.0.0.0", port=5000, debug=True)
>>>>>>> f54b197ef2165530a73ffce1181ccc6d900bf53a
