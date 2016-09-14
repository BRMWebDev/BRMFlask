"""
Load app and run it.

Enables debug and profiler.
"""
from flask_debugtoolbar import DebugToolbarExtension
from werkzeug.contrib.profiler import ProfilerMiddleware

from brmflask.app import create_app

if __name__ == "__main__":
    runapp = create_app(template_folder='tests/dryrun/templates')
    DebugToolbarExtension(runapp)
    # Enabling profiling
    runapp.config['PROFILE'] = True
    # Get 5 most expensive functions
    runapp.wsgi_app = ProfilerMiddleware(
        runapp.wsgi_app, restrictions=[5]
    )
    runapp.run(debug=False)
