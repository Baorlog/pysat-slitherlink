from flask import Flask, request, jsonify, send_from_directory
from solver.pysat_slitherlink_binomal import pysat_slitherlink_binomal

app = Flask(__name__)

PORT = 80
WEB_DIR = "view"


@app.route('/')
def hello_world():
    return send_from_directory(WEB_DIR, )


@app.route('/solve', methods=["POST"])
def test_post():
    slitherlink = request.get_json(force=True)["slitherlink"]

    solution = pysat_slitherlink_binomal(slitherlink)

    return jsonify(solution)


app.run(port=80)

