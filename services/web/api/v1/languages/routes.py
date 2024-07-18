import json
from api.v1 import bp
from flask import jsonify


_data = {
    "Romaninan": "native",
    "Russian": "native",
    "English": "C1",
    "German": "A1",
}


@bp.cli.command("get-languages")
def get_languages_command():
    print(json.dumps(_data, indent=4))


@bp.route("/languages")
def get_languages():
    return jsonify(_data)
