"""
Test brmflask.blueprints.static view functions.

Test all the views in the static blueprint.
"""
import pytest
from flask import url_for


def test_humans(client):
    """Humans.txt should respond with a success 200."""
    response = client.get(url_for('static.humans'))
    assert response.status_code == 200


def test_robots(client):
    """Robots.txt should respond with a success 200."""
    response = client.get(url_for('static.robots'))
    assert response.status_code == 200


@pytest.mark.options(debug=True)
def test_list_configs_no_debug(client):
    """List configs should return only if in debug mode."""
    response = client.get(url_for('static.list_configs'))
    assert response.status_code == 200


@pytest.mark.options(debug=False)
def test_list_configs(client):
    """List configs should always be a 404 unless in debug mode."""
    response = client.get(url_for('static.list_configs'))
    assert response.status_code == 404
