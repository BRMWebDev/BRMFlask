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

    # Inject test redirect routes
    app.config['REDIRECTS'].update({'url/to/redirect': '/'})
    app.config['REDIRECT_KEYS'].append('url/to/redirect')
    return app
