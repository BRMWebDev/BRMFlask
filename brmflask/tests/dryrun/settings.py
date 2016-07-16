"""Various Config classes for BRMFlask app."""
from brmflask.settings import BaseConfig


class LiveConfig(BaseConfig):
    """Alias the BaseConfig to LiveConfig."""

    pass


class TestConfig(BaseConfig):
    """Config for testing (dryrun needs template_path)."""

    TEMPLATE_PATH = 'brmflask/tests/dryrun/templates'


class DevConfig(BaseConfig):
    """DevConfig is the default development env."""

    BASE_URI = 'http://'
    ASSET_SUFFIX = ''
    TEMPLATE_PATH = 'brmflask/tests/dryrun/templates'
    SERVER_NAME = 'brmflask.dissata.com:5000'
    HOSTNAME_LIST = [SERVER_NAME]
    ASSET_BASE = 'http://brmflask.dissata.com'
    ASSET_PATH = '{}/github/brmullikin/BRMFlask/brmflask/tests/dryrun/static/dist'.format(ASSET_BASE)
    DENY_ROBOTS = True
    FLASK_CACHE = {
        'CACHE_DEFAULT_TIMEOUT': 1,
        'CACHE_TYPE': 'null'
    }
