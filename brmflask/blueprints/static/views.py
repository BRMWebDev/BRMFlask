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


# TODO create vcard
# @static.route('/vcard')
# # def vcard():
#     return render_template('/html/vcard.html')


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
    try:
        response = make_response(
            render_template(
                template_path('txt/humans.txt')
            )
        )
        response.headers['Content-type'] = "text/plain"
        return response
    except:
        if current_app.debug:
            raise
        else:
            abort(404)


@static.route('/robots.txt')
def robots():
    """Robot Crawler txt for search engines."""
    try:
        response = make_response(
            render_template(
                template_path('txt/robots.txt')
            )
        )
        response.headers['Content-type'] = "text/plain"
        return response
    except:
        if current_app.debug:
            raise
        else:
            abort(404)
