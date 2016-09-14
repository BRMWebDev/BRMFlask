"""The BRMFlask Sitemap Blueprint."""
from flask import Blueprint

sitemap = Blueprint(
    'sitemap',
    __name__,
    template_folder='templates',
    static_folder='static'
)
from . import views
