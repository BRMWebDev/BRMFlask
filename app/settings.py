"""Various Config classes for BRMFlask app."""
from brmflask.settings import BaseConfig


class LiveConfig(BaseConfig):
    """Alias the BaseConfig to LiveConfig."""

    pass


class DevConfig(BaseConfig):
    """DevConfig is the default development env."""

    BASE_URI = 'http://'
    ASSET_SUFFIX = ''
    SERVER_NAME = 'brmullikin.dissata.com:5000'
    HOSTNAME_LIST = [SERVER_NAME]
    ASSET_BASE = 'http://brmullikin.dissata.com'
    ASSET_PATH = '{}/heroku/brmullikin/static/dist'.format(ASSET_BASE)
    DENY_ROBOTS = True


class HerokuConfig(BaseConfig):
    """HerokuConfig is a staging config."""

    BASE_URI = 'http://'
    ASSET_SUFFIX = ''
    SERVER_NAME = 'brmullikin.herokuapp.com'
    HOSTNAME_LIST = [SERVER_NAME]
    ASSET_BASE = 'https://s3.amazonaws.com/'
    ASSET_PATH = '{}{}'.format(
        ASSET_BASE,
        "static.dissata.com/static.brmullikin.com/dist"
    )
    DENY_ROBOTS = True
