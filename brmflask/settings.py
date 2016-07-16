"""Settings for the BRMFlask app."""
from brmflask.utils.setting_funcs import map_routes


class BaseConfig(object):
    """Default App Config."""

    INCLUDE_VERSION = True

    VERSION = '0.2.1'

    BASE_URI = 'https://'
    # Canonical url for the applciation
    SERVER_NAME = 'www.brmullikin.com'

    # acceptable servers/hosts from which to serve content
    HOSTNAME_LIST = ['www.brmullikin.com']

    # Deny robots? For staging and dev.
    DENY_ROBOTS = False

    # Flask Cache Config
    FLASK_CACHING = {
        'CACHE_DEFAULT_TIMEOUT': 86400,
        'CACHE_TYPE': 'simple'
    }

    SEND_FILE_MAX_AGE_DEFAULT = 43200

    PERMANENT_SESSION_LIFETIME = 2678400

    # Set the encryption key
    SECRET_KEY = "46KQh7MN93ucu2M31Vj8EJwXUY2QCJ"

    ###############
    # Assets Config
    ###############

    # Add .min to assets
    ASSET_SUFFIX = '.min'
    # What is the path for Assets?

    ASSET_BASE = 'https://s3.amazonaws.com/'

    ASSET_PATH = '{}static.brmullikin.com/dist'.format(ASSET_BASE)

    ##################
    # Redirect Configs
    ##################

    # Dictionary of redirects
    REDIRECTS = {}
    # List of keys of redirects (e.g. paths to redirect)
    REDIRECT_KEYS = list(REDIRECTS.keys())

    ##########################
    # Route & Template Configs
    ##########################

    # Path where the template files will be
    TEMPLATE_PATH = 'app/templates'
    SITE_FOLDER = 'site'
    # What are the appropriate extensions for the template files?
    TEMPLATE_EXTENSIONS = ['*.html']
    # ignore template files with this path or name
    TEMPLATE_IGNORE = [
        'home'
    ]

    ROUTES = map_routes(
        template_path="{}/{}".format(TEMPLATE_PATH, SITE_FOLDER),
        template_extensions=TEMPLATE_EXTENSIONS,
        ignore_paths=TEMPLATE_IGNORE
    )
    BRMFLASK_BLUEPRINTS = ['static', 'sitemap', 'dynamic']
    BRMFLASK_EXTENSIONS = ['markdown', 'compress', 'cache']
    MARKDOWN_EXTENSIONS = [
        'footnotes',
        'smarty',
        'toc',
        'attr_list',
        'codehilite',
        'fenced_code'
    ]
    MARKDOWN_CONFIGS = {
        'codehilite': {
            'linenums': True,
            'guess_lang': True
        }
    }
