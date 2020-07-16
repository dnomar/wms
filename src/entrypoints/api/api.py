import sys
sys.path.append(r"C:\Users\van-gerald.olivares\Documents\08 Code\wms")
from  src.app.application.service.bodega.new_bodega_usecase import NewBodegaUseCase
from src.app.infrastructure.domain.bodega.in_memory.in_memory_bodega_repository import InMemoryBodegaRepository
from src.app.application.service.bodega.bodega_request import BodegaRequest
from flask import Flask, jsonify, request, Response


app = Flask(__name__)


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
    print(sys.path)