"""Utilies: Routing helper functions."""
from os.path import isfile, join
from os import getcwd
from flask import current_app


def base_path(path=""):
    """
    Join current working directory with path.

    :param path: <string> path
    :return: <string> joined path
    """
    return join(getcwd(), path)


def template_path(path=""):
    """
    Join the template path with the given path.

    :param path: <string> path
    :param base_path: <string> base_path
    :return: <string> joined path

    # TODO add in check for base_path
    # TODO refactor
    """
    return join(current_app.config['TEMPLATE_PATH'], path)


def site_path(path=""):
    """
    Join the template path, site folder, and a path.

    :param path: <string> path
    :param base_path: <string> base_path
    :return: <string> joined path

    # TODO add in check for base_path
    # TODO refactor
    """
    return "{}/{}/{}".format(
        current_app.config['TEMPLATE_PATH'],
        current_app.config['SITE_FOLDER'],
        path
    )


def route_exists(path):
    """
    Check if routable file exists at path.

    :param path: <string> path
    :return: <string> route OR None
    """
    # need preceeding slash.
    # path = "/{}".format(path)
    # check if path is the ROUTES list app config.
    # If not return None
    if path not in current_app.config['ROUTES']:
        return None
    # Iterate through each extension possibility in TEMPLATE_EXTENSIONS.
    # If the file exists, return the path othe the file
    return template_extension(path)


def template_extension(path):
    """
    Check if file with allowable extension exists for route

    :param path: <string> path
    :return: <string> route OR None
    """
    for ext in current_app.config['TEMPLATE_EXTENSIONS']:
        # Check is lazy, and looks only for the first match
        if isfile(
            '{0}.{1}'.format(
                site_path(path),
                ext[2:]
            )
        ):
            # return if a match is found.
            # [2:] is because of the glob formate for denoting extension ()
            return '{0}.{1}'.format(
                path,
                ext[2:]
            )
    return None
