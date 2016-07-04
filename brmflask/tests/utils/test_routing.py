"""Utilities: test routing utility functions."""
from brmflask.utils import routing
from os import getcwd
from os.path import join


def test_base_path():
    """
    Test base_path joins correctly.

    1. Ensure that path joins correctly.
    2. Ensure that basepath has trailing slash (for consistency,
       since join() adds the trailing slash.).
    3. Same as 2.
    """
    assert routing.base_path('/some/path') == join(getcwd(), '/some/path')
    assert not routing.base_path() == getcwd()
    assert routing.base_path() == join(getcwd(), '')


def test_template_path(config, app):
    """
    Test if template_path joins correctly.

    Ensure that path joins to TEMPLATE_PATH correctly.
    """
    assert (
        routing.template_path('/some/path') ==
        join(config['TEMPLATE_PATH'], '/some/path')
    )


def test_site_path(config, app):
    """
    Test if site_path joins correctly.

    Ensure that path joins to TEMPLATE_PATH correctly.
    """
    assert (
        routing.site_path('/some/path') ==
        "{}/{}/{}".format(
            config['TEMPLATE_PATH'],
            config['SITE_FOLDER'],
            '/some/path'
        )
    )


def test_route_exists(config, app):
    """Test route_exists function."""
    assert routing.route_exists('Some/fake/file') is None
    config['ROUTES'].append('some/other/file')
    assert 'some/other/file' in config['ROUTES']
    assert routing.route_exists('Some/other/file') is None
    for r in config['ROUTES']:
        routed = routing.route_exists(r)
        if routed is None:
            pass
        elif routed[-5:] == ".html":
            assert routed == "{}.html".format(r)
