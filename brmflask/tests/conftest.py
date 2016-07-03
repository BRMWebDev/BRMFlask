"""Initialize flask app for pytest."""
import pytest

from brmflask.app import create_app


@pytest.fixture
def app():
    """Create testing application."""
    params = {
        'DEBUG': False,
        'TESTING': True,
        'BRMFLASK_CONFIG': 'app.settings.LiveConfig',
        'BRMFLASK_TEST_KEY': 'TEST_VALUE'
    }

    app = create_app(config_override=params)
    return app
