from brmflask.utils.routing import base_path
from flask import Blueprint

static = Blueprint(
    'static',
    __name__,
    template_folder=base_path(),
    static_folder='static'
)

from . import views
