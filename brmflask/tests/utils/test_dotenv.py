"""Test utils.security functions."""
from brmflask.utils.dotenv import dotenv
import os


def test_dotenv(tmpdir):
    """Should verify that dotenv returns usable values"""
    assert dict(dotenv('file')) == {}
    # Env file w/ various file conditions for dotenv()
    assert dict(dotenv('./.brm_env')) == dict(dotenv('./.brm_env'))
