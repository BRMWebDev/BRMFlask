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
