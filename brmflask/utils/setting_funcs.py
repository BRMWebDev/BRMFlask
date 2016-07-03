"""Utilites: Functions to Help configure the BaseConfig class."""
import os
import fnmatch


def map_routes(
    template_path,
    template_extensions,
    ignore_paths
):
    """Generate routes from a folder directory."""
    routes = []
    for root, dirnames, filenames in os.walk(template_path):
        for extension in template_extensions:
            for filename in fnmatch.filter(filenames, extension):
                root = root.replace(template_path, "")
                route = os.path.join(root, filename[:-len(extension[1:])])
                if "/" in route[:1]:
                    route = route[1:]
                if route not in ignore_paths:
                    routes.append(route)
    return routes
