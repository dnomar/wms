from flask import Flask, jsonify, request, Response
from src.app.domain import commands
from src.app.service import messagebus, unit_of_work

app = Flask(__name__)


@app.route("/hello_world", methods=['GET'])
def allocate_endpoint():
    return jsonify({"message": "hello world"}), 200


@app.route("/create_warehouse", methods=['POST'])
def create_warehouse():
    wh_ref = request.json['wh_ref']
    cmd=commands.CreateWarehouse(wh_ref)
    uow=unit_of_work.FakeWarehouseUnitofWork()
    messagebus.handle(cmd,uow)
    return 'OK', 201


@app.route("/get_wh_master", methods=['POST'])
def get_warehouse_master():
    pass


@app.route("/", methods=['GET'])
def get_version():
    data={
        "Title":"Symplex WMS",
        "License":"SLI Standard License",
        "Version":"1.0.0-Beta"
    }
    return jsonify(data), 200