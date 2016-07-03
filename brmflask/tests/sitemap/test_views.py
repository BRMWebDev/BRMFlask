"""
Test brmflask.blueprints.sitemap view functions.

Test all the views in the sitemap blueprint.
"""
from flask import url_for


def test_sitemap(client):
    """Sitemap should respond with a success 200."""
    response = client.get(url_for('sitemap.sitemap'))
    assert response.status_code == 200
