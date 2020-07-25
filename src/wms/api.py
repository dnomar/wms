from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/create_warehouse", methods=['GET'])
def create_warehouse():

    return jsonify({"message": "Funciona la API"}), 200
