from flask import Blueprint

bp = Blueprint("v1", __name__)

from .main import routes
from .contact import routes
from .summary import routes
from .skills import routes
from .experience import routes
from .education import routes
from .languages import routes
