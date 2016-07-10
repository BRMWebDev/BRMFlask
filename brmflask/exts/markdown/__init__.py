from flask_markdown import Markdown

def register_markdown(app):
    from brmflask.exts.markdown import mdx_span_classes
    md = Markdown(
        app,
        extensions=app.config['MARKDOWN_EXTENSIONS'],
        extension_configs=app.config['MARKDOWN_CONFIGS'],
        auto_reset=True
    )
    md.register_extension(mdx_span_classes.makeExtension)
    return md
