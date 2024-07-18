import json
from api.v1 import bp
from flask import jsonify


_data = {
    "api": {
        "title": "Calin Radu -- CV",
        "version": "1.0.0",
        "description": "The simple, yet helpful API that describes Calin's experience",
    },
}


@bp.cli.command("get-api-info")
def get_api_info_command():
    print(json.dumps(_data, indent=4))


@bp.route("/")
def get_api_info():
    return jsonify(_data)
