"""
Extensions: Load the Flask Debug Toolbar.

BEWARE: App is set to debug mode so FDT can run.
"""
from flask_debugtoolbar import DebugToolbarExtension

def register_debug_toolbar(app):
    """Register the Debug Toolbar extension."""
    DebugToolbarExtension(app)
    return app
