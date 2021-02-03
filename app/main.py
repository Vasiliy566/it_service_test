import flask
from flask import request, jsonify
import logging
import numpy as np

from app.src.common.common import no_request_argument_provided_error, wrong_type_argument_provided
from app.src.find_distance import reformat_adj_matrix, dijkstra

logger = logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

app = flask.Flask(__name__)
app.config["DEBUG"] = True
get_distance_args = {"city_start": int, "city_finish": int}


@app.route('/get_distance', methods=['GET'])
def get_distance():
    # Проверка api-ключа
    # TODO: сравнивать хеш вместо самого ключа
    if "X-Api-Key" not in request.args or not request.args["X-Api-Key"] == '123321':
        resp = jsonify({"message": "ERROR: Unauthorized"})
        resp.status_code = 401
        return resp

    args = {}  # {названия агрументов : отформатированные значения}
    for k, v in get_distance_args.items():
        if k not in request.args:
            return no_request_argument_provided_error(k)
        try:
            args[k] = v((request.args[k]))
        except Exception as e:
            logger.error(e)
            return wrong_type_argument_provided(k, v)

    distances = reformat_adj_matrix(np.load(open("data/matrix_distance", "rb")))
    try:
        distance, path = dijkstra(args["city_start"], args["city_finish"], distances)
    except Exception as e:
        logger.error(e)
        resp = jsonify({"body": str(e)})
        resp.status_code = 422
        return resp
    resp = jsonify({
        "body": {
            "path": path,
            "distance": distance
        }})
    resp.status_code = 200
    return resp


app.run()
