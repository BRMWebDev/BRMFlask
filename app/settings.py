"""Various Config classes for BRMFlask app."""
from brmflask.settings import BaseConfig


class LiveConfig(BaseConfig):
    """Alias the BaseConfig to LiveConfig."""

    pass


class DevConfig(BaseConfig):
    """DevConfig is the default development env."""

    BASE_URI = 'http://'
    ASSET_SUFFIX = ''
    SERVER_NAME = 'brmflask.dissata.com:5000'
    HOSTNAME_LIST = [SERVER_NAME]
    ASSET_BASE = 'http://brmflask.dissata.com'
    ASSET_PATH = '{}/github/brmflask/static/dist'.format(ASSET_BASE)
    DENY_ROBOTS = True
