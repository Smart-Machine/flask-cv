import json
from api.v1 import bp
from flask import jsonify


_data = {
    "summary": (
        "Experienced software developer with a passion for"
        "creating smart solutions and optimizing performance."
        "Equipped with a solid foundation in software engineer"
        "ing principles, I flourish in dynamic environments where "
        "creativity meets technical precision."
    )
}


@bp.cli.command("get-summary")
def get_summary_command():
    print(json.dumps(_data, indent=4))


@bp.route("/summary")
def get_summary():
    return jsonify(_data)
