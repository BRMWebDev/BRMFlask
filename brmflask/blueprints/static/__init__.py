from flask import Blueprint

static = Blueprint(
    'static',
    __name__,
    template_folder='templates',
    static_folder='static'
)

from . import views
