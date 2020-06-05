from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/hello_world", methods=['GET'])
def allocate_endpoint():
    return jsonify({"message": "Funciona la API"}), 200
