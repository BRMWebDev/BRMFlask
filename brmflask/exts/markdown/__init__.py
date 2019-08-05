from brmflask.exts.markdown.markdown import Markdown


def register_markdown(app):
    md = Markdown(
        app,
        extensions=app.config['MARKDOWN_EXTENSIONS'],
        extension_configs=app.config['MARKDOWN_CONFIGS'],
        auto_reset=True
    )
    return md
