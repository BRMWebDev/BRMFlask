"""Coverage Command."""
import subprocess

import click


@click.command()
@click.argument('path', default='brmflask')
def cli(path):
    """
    Run a test coverage report.

    :param path: Test coverage path
    :return: Subprocess call result
    """
    cmd = 'py.test -v --cov-report term-missing --cov {0}'.format(path)
    return subprocess.call(cmd, shell=True)
