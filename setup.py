from setuptools import setup

setup(
    name='BRMFlask',
    version='0.2.1',
    url='http://github.com/brmullikin/brmflask',
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
        'flask_cache',
        'flask_markdown',
        'coloredlogs',
        'htmlmin',
        'Markdown',
        'smartypants',
        'dotenv',
        'pygments'
    ],
    dependency_links=[
        'git+git://github.com/sh4nks/flask-cache.git#egg=flask_cache',
        'git+git://github.com/brmullikin/flask-markdown.git@0.4#egg=flask_markdown'
    ]
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
