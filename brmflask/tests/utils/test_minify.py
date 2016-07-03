"""Utilities: test routing utility functions."""
import pytest
from brmflask.utils import minify
from htmlmin import minify as _minify


@minify.minify_response
def minify_func(html_template):
    """Humans.txt should respond with a success 200."""
    return html_template

html_template = """<!doctype html>
                    <html lang="en">
                    <head>
                      <meta charset="utf-8">
                      <title>The HTML</title>
                    </head>
                    <body>
                    <h1>Html Page</h1>
                    </body>
                    </html>"""


@pytest.mark.options(debug=True)
def test_minify_debug(client):
    """No minify if in debug mode."""
    assert minify_func(html_template) == html_template
    assert not minify_func(html_template) == _minify(html_template)


def test_minify(client):
    """
    Test if the minify decorator minifies.

    1. Assert reponse and compare to minify.
    """
    assert "minify" == _minify("minify")
    assert "minify" == minify_func("minify")
    assert not minify_func(html_template) == html_template
    assert minify_func(html_template) == _minify(html_template)
