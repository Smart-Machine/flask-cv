import json
from api.v1 import bp
from flask import jsonify


_data = {
    "05/2024 – present": {
        "title": "Middle Backend Developer",
        "company": "Simpals",
        "tech": [
            "Tornado",
            "ElasticSearch",
            "MongoDB",
            "Python",
            "Golang",
            "gRPC",
            "GraphQL",
            "Redis",
            "Docker",
        ],
        "achievements": [
            (
                "Participate in the migration of monolithic product, "
                "called 999 written in Python 2.3, towards microservices in Golang."
            ),
            "Maintaining the big monolithic product, called 999.md",
        ],
    },
    "03/2022 – 04/2024": {
        "title": "Software Developer",
        "company": "CIAL Dun & Bradstreet",
        "tech": [
            "Python",
            "Scrapy",
            "Docker",
            "Playwright",
            "Redis",
            "MongoDB",
            "Splash",
            "Javascript",
            "Bash",
        ],
        "achievements": [
            "Developed and maintained a collection of web scrapers.",
            (
                "Introduced major changes into the project, like the integration "
                "of a modern headless browser replacing dozens of deprecated "
                "dependencies, which halved the time for developing a data miner."
            ),
            (
                "During my last year of work, a coverage of 99.8% of data was "
                "achieved due to the radical changes brought in the project, "
                "which was the highest score ever reached in the company."
            ),
        ],
    },
    "02/2021 – 02/2022": {
        "title": "Software Engineer",
        "company": "SmartSoftDev",
        "tech": [
            "C++",
            "Python",
            "React",
            "Bash",
        ],
        "achievements": [
            (
                "Developed a low-level, simplified reverse proxy for medical device "
                "farm, as a replacement for Nginx"
            ),
            (
                "Participated in the migration of UI, from a static HTML to responsive "
                "React, for the medical device farm."
            ),
            (
                "Participated in the development of web-socket architecture and migration "
                "for the medical device farm."
            ),
        ],
    },
    "04/2020 – 02/2021": {
        "title": "Backend Developer",
        "company": "Light Square Development",
        "tech": [
            "Golang",
            "PostgreSQL",
        ],
        "achievements": [
            "Participated in the server-side development of a warehouse management system",
            "Managed enpoints, developed the RBAC system, managed database",
        ],
    },
}


@bp.cli.command("get-experience")
def get_experience_command():
    print(json.dumps(_data, indent=4))


@bp.route("/experience")
def get_experience():
    return jsonify(_data)
