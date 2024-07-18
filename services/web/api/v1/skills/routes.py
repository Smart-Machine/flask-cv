import json
from api.v1 import bp
from flask import jsonify


_data = {
    "skills": {
        "languages": ["Python", "JavaScript", "Go", "C++", "SQL", "Bash"],
        "technologies": [
            "Docker",
            "Linux",
            "React",
            "Scrapy",
            "Playwright",
            "REST",
            "gRPC",
            "RabbitMQ",
            "Websockets",
        ],
    },
}


@bp.cli.command("get-skills")
def get_skills_command():
    print(json.dumps(_data, indent=4))


@bp.route("/skills")
def get_skills():
    return jsonify(_data)
