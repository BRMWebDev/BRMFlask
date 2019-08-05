"""
Convert string to markdown.

flask_markdown
~~~~~~~~~~~~~~~~~

Originally from: https://github.com/dcolish/flask-markdown

This version can be found at: https://github.com/brmullikin/flask-markdown

Markdown filter class for Flask
To use::

    from flask_markdown import Markdown
    md = Markdown(app)

Then in your template::

    {% filter markdown %}
    Your Markdown
    =============
    {% endfilter %}

You can also do::

    {{ mymarkdown|markdown}}


Optionally, you can keep a reference to the Markdown instance and use that
to register custom extensions by calling :func:`register_extension` or
decorating the extension class with :func:`extend`

:copyright: (c) 2013 by Dan Colish.
:license: BSD, MIT see LICENSE for more details.
"""

from __future__ import absolute_import
from flask import Markup
from jinja2 import evalcontextfilter, escape
import markdown as md
from markdown import (
    blockprocessors,
    Extension,
    preprocessors,
)
__all__ = ('blockprocessors', 'Extension', 'Markdown', 'preprocessors')


class Markdown(object):
    """
    Wraps markdown objects.

    Simple wrapper class for Markdown objects, any options that are available
    for markdown may be passed as keyword arguments like so::

      md = Markdown(app,
                    auto_escape=False,
                    auto_reset=False,
                    extensions=['footnotes'],
                    extension_configs={
                        'footnotes': ('PLACE_MARKER','~~~~~~~~')
                    },
                    safe_mode=True,
                    output_format='html4'
                   )

    You can then call :func:`register_extension` to load custom extensions into
    the Markdown instance or use the :func:`extend` decorator

    Additionally, passing auto_escape=True will cause the Markdown filter to
    obey the Jinja2 auto_escape parameter in the context of the filter
    evaluation. By default, this is disabled, and the content passed to the
    Markdown filter will not be escaped.

    :param app: Your Flask app instance
    :param bool auto_escape: Obey Jinja2 auto_escaping, defaults to False
    :param markdown_options: Keyword args for the Markdown instance
    """

    def __init__(
        self,
        app=None,
        auto_escape=False,
        auto_reset=False,
        **markdown_options
    ):
        """Markdown uses old style classes."""
        self.auto_escape = auto_escape
        self.auto_reset = auto_reset
        self._instance = md.Markdown(**markdown_options)

        if app is not None:
            self._init_extension(app)

    def _init_extension(self, app):
        """
        Initialize with app and add as an extension.

        1. If it doesn't already exist, add extension attribute.
        2. Set the markdown extension to the extensions attribute.
        3. Add the Jinja2 filter.
        """
        if not hasattr(app, 'extensions'):
            app.extensions = {}
        app.extensions['markdown'] = self
        app.jinja_env.filters.setdefault(
            'markdown', self.__build_filter(self.auto_escape)
        )

    def __call__(self, stream):
        """When Markdown is called."""
        if self.auto_reset:
            self._instance.reset()
        return Markup(self._instance.convert(stream))

    def __build_filter(self, app_auto_escape):
        @evalcontextfilter
        def markdown_filter(eval_ctx, stream):
            """
            Filter Jinja2 text.

            Called by Jinja2 when evaluating the Markdown filter. Utilizes the
            Markdown instance stored in the Flask app config.

            :param eval_ctx: Evaluation context from Jinja2, used for
                             auto_escape
            :param stream: Content passed to the filter
            """
            __filter = self
            if app_auto_escape and eval_ctx.autoescape:
                return Markup(__filter(escape(stream)))
            else:
                return Markup(__filter(stream))
        return markdown_filter

    def extend(self, configs=None):
        """
        Decorator for registering macros.

        You must either force the decorated class to be imported
        or define it in the same file you instantiate Markdown.
        To register a simple extension you could do::

          from flask_markdown import Extension, Markdown
          from preprocessors import SimplePreprocessor
          markdown_instance = Markdown(app)

          @markdown_instance.make_extension()
          class SimpleExtension(Extension):
               def extendMarkdown(self, md, md_globals):
               md.preprocessors.add('prover_block',
                                    SimplePreprocessor(md),
                                    '_begin')
               md.registerExtension(self)

        :param configs: A dictionary of options for the extension being
                        registered
        """
        def decorator(ext_cls):
            return self.register_extension(ext_cls, configs)
        return decorator

    def register_extension(self, ext_cls, configs=None):
        """
        Register Markdown extension.

        This will register an extension class with self._instance. You may pass
        any additional configs required for your extension

        It is best to call this when starting your Flask app, ie.::

          from .mdx_simpl import SimpleExtension

          md = Markdown(app)
          md.register_extension(SimpleExtension)

        Any additional configuration arguments can be added to configs and will
        be passed through to the extension you are registering

        :param configs: A dictionary of options for the extension being
                        regsitered
        :param ext_cls: The class name of your extension
        """
        instance = ext_cls()
        self._instance.registerExtensions([instance], configs)
        return ext_cls
