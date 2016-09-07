"""Extensions: Call the Flask_Cache plugin."""
from flask_caching import Cache

cache = Cache()

def register_cache(app, cache):
    """Register the cache extension."""
    cache.init_app(app, config=app.config['FLASK_CACHING'])
    return cache
