"""
Test brmflask.app functions.

Test all functions in brmflask.app. We will omit tests
for create_app() and configure_app() since they are prerequisite
for all other Flask related tests.
"""
from brmflask.app import load_env
from brmflask.utils.dotenv import dotenv
from os import environ


def test_env_load(client):
    """Home page should respond with a success 200."""
    assert dict(load_env('./.brm_env')) == dict(dotenv('./.brm_env'))
    assert dict(load_env('file')) == {}


def test_app(config, app):
    """
    Verify app loads correctly.

    1. Make sure we are not in debug mode.
    2. Make sure we are loading the correct settings class.
    3. Make sure we are able to access ENV variables as expected
       And that they can be overriden by configs_overriden when
       app is instantiated.
    """
    config_class_string = "brmflask.tests.dryrun.settings.TestConfig"
    assert not app.debug
    assert config['BRMFLASK_CONFIG'] == config_class_string
    assert config['BRMFLASK_TEST_KEY'] == "TEST_VALUE"
    assert config['BRMFLASK_ENV_FILE'] == ".brm_env"
