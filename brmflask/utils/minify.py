"""Utilites: minify response decorator."""
from htmlmin import minify
from functools import wraps
from flask import current_app


def minify_response(f):
    """Minify the current output."""
    @wraps(f)
    def wrapped(*args, **kwargs):
        if current_app.debug:
            return f(*args, **kwargs)
        else:
            return minify(f(*args, **kwargs))
    return wrapped
