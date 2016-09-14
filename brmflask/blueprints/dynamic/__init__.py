"""The BRMFlask Dynamic Blueprint."""
from brmflask.utils.routing import base_path
from flask import Blueprint

dynamic = Blueprint(
    'dynamic',
    __name__,
    template_folder=base_path(),
    static_folder='static'
)
from . import views
