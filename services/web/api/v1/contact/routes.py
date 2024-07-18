import json
from api.v1 import bp
from flask import jsonify


_data = {
    "phone": "+373 60057214",
    "address": "Chisinau, Moldova",
    "email": "radu.calin500@gmail.com",
    "github": "github.com/Smart-Machine",
}


@bp.cli.command("get-contact")
def get_contact_info_command():
    print(json.dumps(_data, indent=4))


@bp.route("/contact")
def get_contact_info():
    return jsonify(_data)
