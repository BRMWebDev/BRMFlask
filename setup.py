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
        'https://github.com/brmullikin/flask-markdown/tarball/master#egg=brmflask_markdown-0.4'
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
