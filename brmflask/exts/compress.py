from flask_compress import Compress

def register_compress(app):
    Compress(app)
    return app
