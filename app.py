import sys

from flask import Flask, request, jsonify, send_from_directory
from solver.pysat_slitherlink_binomal import pysat_slitherlink_binomal

PORT = 80
WEB_DIR = "view"


app = Flask(__name__, static_folder=WEB_DIR)


@app.route('/')
def hello_world():
    return send_from_directory(WEB_DIR, "index.html")


@app.route('/solve', methods=["POST"])
def test_post():
    slitherlink = request.get_json(force=True)['slitherlink']
    # print(slitherlink, file=sys.stderr)

    success, solution, time, clauses, var_num, loop = pysat_slitherlink_binomal(slitherlink)

    if success:
        return jsonify({
            'success': success,
            'solution': solution,
            'time': time,
            'clause': clauses,
            'var': var_num,
            'loop': loop
        })
    else:
        return jsonify({
            'success': success
        })


app.run(port=PORT, debug=True)

