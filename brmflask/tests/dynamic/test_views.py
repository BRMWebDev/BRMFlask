"""
Test brmflask.blueprints.dynamic view functions.

Test all the views in the dynamic blueprint.
"""
from flask import url_for


def test_homepage(client):
    """Homapage should respond with a success 200."""
    response = client.get(url_for('dynamic.homepage'))
    assert response.status_code == 200


def test_router(config, client):
    """Respond config['ROUTES'] with a success 200."""
    # Test for ordinary routing ability
    for r in config['ROUTES']:
        response = client.get(url_for('dynamic.router', path=r))
        assert response.status_code == 200

    # Test 404 if not a valid route
    assert client.get(
        url_for(
            'dynamic.router',
            path='some/fake/path'
        )
    ).status_code == 404


def test_redirect(config, client):
    """Determine if Redirects are correctly being rerouted."""
    for r in config['REDIRECTS']:
        response = client.get(url_for('dynamic.router', path=r))
        assert response.status_code == 301
