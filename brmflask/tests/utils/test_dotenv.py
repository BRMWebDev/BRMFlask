"""Test utils.security functions."""
from brmflask.utils.dotenv import dotenv
import os


def test_dotenv(tmpdir):
    """Should verify that dotenv returns usable values"""
    assert dict(dotenv('file')) == {}
