"""Blueprint: static views."""
from flask import (
    make_response,
    render_template,
    jsonify,
    current_app,
    abort
)
from brmflask.utils.routing import template_path
from . import static


@static.route('/list-configs')
def list_configs():
    """Return the config dictionary if in Debug mode."""
    if current_app.debug:
        return jsonify(current_app.config)
    else:
        abort(404)


@static.route('/humans.txt')
def humans():
    """Return Humans readable information about the website."""
    if current_app.config['STATIC_ROUTES'].get('humans', None):
        response = make_response(
            render_template(
                template_path(current_app.config['STATIC_ROUTES']['humans'])
            )
        )
        response.headers['Content-type'] = "text/plain"
        return response
    else:
        abort(404)


@static.route('/robots.txt')
def robots():
    """Robot Crawler txt for search engines."""
    if current_app.config['STATIC_ROUTES'].get('robots', None):
        response = make_response(
            render_template(
                template_path(current_app.config['STATIC_ROUTES']['robots'])
            )
        )
        response.headers['Content-type'] = "text/plain"
        return response
    else:
        abort(404)
