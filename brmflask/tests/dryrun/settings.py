"""Various Config classes for BRMFlask app."""
from brmflask.settings import BaseConfig
from brmflask.utils.setting_funcs import map_routes


class LiveConfig(BaseConfig):
    """Alias the BaseConfig to LiveConfig."""

    pass


class TestConfig(BaseConfig):
    """Config for testing (dryrun needs template_path)."""

    TEMPLATE_PATH = 'brmflask/tests/dryrun/templates'

    # Routes can be added manually or generated.
    ROUTES = map_routes(
        template_path="{}/{}".format(TEMPLATE_PATH, BaseConfig.SITE_FOLDER),
        template_extensions=BaseConfig.TEMPLATE_EXTENSIONS,
        ignore_paths=BaseConfig.TEMPLATE_IGNORE
    )


class DevConfig(BaseConfig):
    """DevConfig is the default development env."""

    BASE_URI = 'http://'
    ASSET_SUFFIX = ''
    SERVER_NAME = 'brmflask.dissata.com:5000'
    HOSTNAME_LIST = [SERVER_NAME]
    ASSET_BASE = 'http://brmflask.dissata.com'
    ASSET_PATH = '{}/github/brmullikin/BRMFlask/brmflask/tests/dryrun/static/dist'.format(
        ASSET_BASE
    )
    DENY_ROBOTS = True
    FLASK_CACHING = {
        'CACHE_DEFAULT_TIMEOUT': 1,
        'CACHE_TYPE': 'null'
    }
    TEMPLATE_PATH = 'brmflask/tests/dryrun/templates'
    ROUTES = map_routes(
        template_path="{}/{}".format(TEMPLATE_PATH, BaseConfig.SITE_FOLDER),
        template_extensions=BaseConfig.TEMPLATE_EXTENSIONS,
        ignore_paths=BaseConfig.TEMPLATE_IGNORE
    )
