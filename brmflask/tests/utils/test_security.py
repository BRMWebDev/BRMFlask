"""Test utils.security functions."""
from flask import url_for


def test_verify_host(client):
    """Should prevent loading of websites with incorrect host."""
    response = client.get(
        url_for('static.humans'),
        headers=[
            ('Host', 'Somehost')
        ]
    )
    assert response.status_code == 404
