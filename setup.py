"""BRMFlask is a unified website generator."""
from setuptools import setup
from brmflask.settings import BaseConfig

MARKDOWN_REPO = "https://github.com/brmullikin/flask-markdown"
REPO = 'http://github.com/brmullikin/brmflask'

setup(
    name='BRMFlask',
    version=BaseConfig.VERSION,
    url=REPO,
    license='None',
    author='B. R. Mullikin',
    author_email='ben@brmullikin.com',
    description='Private Flask App',
    long_description=__doc__,
    packages=['brmflask'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask',
        'Flask-Compress',
        'flask_caching',
        'brmflask_markdown==0.4',
        'coloredlogs',
        'htmlmin',
        'Markdown',
        'smartypants',
        'dotenv',
        'pygments'
    ],
    dependency_links=[
        '{}/tarball/master#egg=brmflask_markdown-0.4'.format(MARKDOWN_REPO)
    ],
    tests_require=[
        'pytest',
        'pytest-flask',
        'pytest',
        'pytest-cov',
        'pytest-flask',
        'pep8',
        'flake8-pep257'
    ]
)
