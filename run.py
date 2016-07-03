"""
Load app and run it.

Enables debug and profiler.
"""
from flask_debugtoolbar import DebugToolbarExtension
from app import runapp

if __name__ == "__main__":
    DebugToolbarExtension(runapp)
    runapp.run(debug=True)
