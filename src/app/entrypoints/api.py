from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/hello_world", methods=['GET'])
def allocate_endpoint():
    return jsonify({"message": "Funciona la API"}), 200


@app.route("/new_warehouse", methods=['POST'])
def create_warehouse():
    wh_ref = request.json['wh_ref']
    print(wh_ref)
    return jsonify({"Warehouse": wh_ref}), 200


@app.route("/get_wh_master", methods=['POST'])
def get_warehouse_master():
    pass


@app.route("/symplex", methods=['GET'])
def get_version():
    data={
        "Title":"Symplex WMS",
        "License":"SLI Standard License",
        "Version":"1.0.0-Beta"
    }
    return jsonify(data), 200