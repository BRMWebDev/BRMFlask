"""
BRMFlask instance instantiation.

Load and configure brmflask flask application.
"""
from os import environ
from importlib import import_module
from flask import Flask
from brmflask.utils.routing import base_path
from dotenv import Dotenv


def create_app(
    app_name=__name__,
    config_override=None,
    env_file='.brm_env',
    template_folder='app/templates'
):
    """
    Create Flask app using factory.

    :param app_name: Name of current application
    :return: Flask Class
    """
    this_app = Flask(
        app_name,
        instance_relative_config=True,
        template_folder=base_path(template_folder)
    )
    configure_app(
        this_app,
        config_override=config_override,
        env_file=env_file
    )
    register_blueprints(this_app, this_app.config['BRMFLASK_BLUEPRINTS'])
    register_extensions(this_app, this_app.config['BRMFLASK_EXTENSIONS'])
    return this_app


def register_blueprints(app, blueprints):
    """
    Apply extensions to Flask app.

    Each extension specified in the extensions list will be called.
    In addition, custom extensions may be put in app/__init__.py.

    Current list options are:
    1. static
    2. sitemap
    3. dynamic

    Psuedo Code:
    1. For each "blueprint" in the list of blueprints
    2. Import the module found at the path brmflask.blueprints."blueprint"
    3. Get the package of the above imported module whose name is "blueprint"
    4. Register the package as a Blueprint object for the given app.

    :param: app Flask app
    :param: extensions list of extensions to add
    :return: None (or is it better to return the app??)
    """
    for blueprint in blueprints:
        app.register_blueprint(
            getattr(
                import_module("brmflask.blueprints.{0}".format(blueprint)),
                blueprint
            )
        )
    return None


def register_extensions(app, extensions):
    """
    Apply extensions to Flask app.

    Each extension specified in the extensions list will be called.
    In addition, custom extensions may be put in app/__init__.py.

    Current options are:
    1. markdown
    2. compress
    3. cache

    :param: app Flask app
    :param: extensions list of extensions to add
    :return: None (or is it better to return the app??)
    """

    for extension in extensions:
        register = "register_{0}".format(extension)
        locals()[register] = getattr(
            import_module("brmflask.exts.{}".format(extension)),
            "register_{}".format(extension)
        )(app)
    return None

def configure_app(app, config_override=None, env_file='.brm_env'):
    """
    Configure application settings.

    :param app: Flask application instance
    :return: Flask app.config object.
    """
    env = load_env(env_file)
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
