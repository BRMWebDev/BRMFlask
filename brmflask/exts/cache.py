"""Extensions: Call the Flask_Cache plugin."""
from flask_caching import Cache
from functools import wraps
from flask import current_app

cache = Cache()

def register_cache(app):
    """Register the cache extension."""
    cache.init_app(app, config=app.config['FLASK_CACHING'])
    return cache


def cached(f):
    """Cache the current output."""
    @wraps(f)
    def wrapped(*args, **kwargs):
        if 'cache' in current_app.config['BRMFLASK_EXTENSIONS']:
            return cache.cached()(f)(*args, **kwargs)
        else:
            return f(*args, **kwargs)
    return wrapped
