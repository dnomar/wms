import sys
sys.path.append(r"C:\Users\van-gerald.olivares\Documents\08 Code\wms")
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
   app.run(
       host="0.0.0.0",
       port=5000,
       debug=True
   )