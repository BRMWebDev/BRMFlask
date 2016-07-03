"""
BRMFlask instance instantiation.

Load and configure brmflask flask application.
"""
from os import environ
from flask import Flask
from flask_compress import Compress
from flask_markdown import Markdown
from brmflask.blueprints.static import static
from brmflask.blueprints.sitemap import sitemap
from brmflask.blueprints.dynamic import dynamic
from brmflask.utils.routing import base_path
from dotenv import Dotenv


def create_app(app_name=__name__, config_override=None):
    """
    Create Flask app using factory.

    :param app_name: Name of current application
    :return: Flask Class
    """
    this_app = Flask(
        app_name,
        instance_relative_config=True,
        template_folder=base_path('app/templates')
    )
    configure_app(this_app, config_override)
    this_app.register_blueprint(static)
    this_app.register_blueprint(sitemap)
    this_app.register_blueprint(dynamic)
    Markdown(
        this_app,
        extensions=[
            'footnotes',
            'wikilinks',
            'smarty',
            'toc',
            'attr_list'
        ],
        auto_reset=True
    )
    Compress(this_app)
    return this_app


def configure_app(app, config_override=None):
    """
    Configure application settings.

    :param app: Flask application instance
    :return: Flask app.config object.
    """
    env = load_env('./.brm_env')
    # ^^ Load environment:
    # load environment from file if it exists
    # OR load from os.environ

    # Add the environ dict to the config
    app.config.update(env)

    # Override any values if necessary
    if config_override:
        app.config.update(config_override)

    # Try to load the class settings specified in the
    # Environ key BRMFLASK_CONFIG
    # These values should be sensetive info, not settings
    # And the values will be applied circularly to the settings.
    app.config.from_object(
        app.config.get(
            'BRMFLASK_CONFIG',
            'brmflask.settings.BaseConfig'
        )
    )
    return app.config


def load_env(env_file):
    """
    Load the app environment.

    First try to load the environment from env file
    If no env file is loaded, then set the env to the
    system environment. This env file will be used to
    load the correct settings class. We are looking for
    the BRMFLASK_CONFIG key which should have the value
    of the class object to load into the config.

    :param env_file: <string> path/to/file
    :return: <dict>
    """
    try:
        # is there a .env file?
        env = Dotenv(env_file)
    except IOError:
        # can't find file try normal environment
        env = environ
    return env
