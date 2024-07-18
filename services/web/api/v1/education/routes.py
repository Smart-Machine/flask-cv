import json
from api.v1 import bp
from flask import jsonify


_data = {
    " - 06/2025": {
        "pursued": "Bachelor of Science in Software Engineering",
        "place": "The Technical University of Moldova",
        "details": [
            (
                "Software Engineering Bachelor Degree, that includes "
                "several branches of math, theory based computer science, and much more. "
                "The speciality of this degree is the PBL (Project Base Learning), thus "
                "most of the acquired knowledge are the result of a finished project."
            ),
        ],
    },
    "02/2023 - 02/2023": {
        "pursued": "Advanced React Certificate",
        "place": "Coursera",
        "details": [
            (
                "Create robust and reusable components with advanced techniques and "
                "learn different patterns to reuse common behavior."
            ),
            "Interact with a remote server and fetch and post data via an API",
            "Seamlessly test React applications with React Testing Library.",
            "Integrate commonly used React libraries to streamline your application development",
        ],
    },
    "01/2023 - 01/2023": {
        "pursued": "React Basics Certificate",
        "place": "Coursera",
        "details": [
            "Use reusable components to render views where data changes over time",
            "Organize React projects to create more scalable and maintainable websites and apps",
            (
                "Use props to pass data between components. Create dynamic and interactive "
                "web pages and apps"
            ),
            "Use forms to allow users to interact with the app. Build an application in React",
        ],
    },
    "01/2023 - 1/2023": {
        "pursued": "Programming with JavaScript Certificate",
        "place": "Coursera",
        "details": [
            "Creating simple JavaScript codes.",
            "Creating and manipulating objects and arrays.",
            "Writing unit tests using Jest.",
        ],
    },
}


@bp.cli.command("get-education")
def get_education_command():
    print(json.dumps(_data, indent=4))


@bp.route("/education")
def get_education():
    return jsonify(_data)
