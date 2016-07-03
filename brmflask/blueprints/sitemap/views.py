"""Blueprint: sitemap views."""
from flask import (
    make_response,
    render_template,
    current_app,
)
from . import sitemap


@sitemap.route('/sitemap.xml')
def sitemap():
    """Generate and return a sitemap."""
    response = make_response(
        render_template(
            'xml/sitemap.xml',
            base="{}{}".format(
                current_app.config.get('BASE_URI'),
                current_app.config.get('SERVER_NAME')
            ),
            routes=current_app.config.get('ROUTES')
        )
    )
    response.headers['Content-type'] = "application/xml"
    return response
