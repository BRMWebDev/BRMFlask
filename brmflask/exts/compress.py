"""Extensions: Call the Flask_Compress plugin."""
from flask_compress import Compress

def register_compress(app):
    """Register the compress extension."""
    Compress(app)
    return app
