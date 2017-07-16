"""Utilites: Functions to help load environment variables."""
from ast import literal_eval
from os.path import exists

def dotenv(path):
    if not exists(path):
        return
    for line in open(path):
        line = line.strip()
        # Ignore comments and lines w/ out equal sign.
        if line.startswith('#') or '=' not in line:
            continue

        # Split key and value, max splits = 1
        key, value = line.split('=', 1)

        # Remove any leading and trailing spaces in key, value
        key, value = key.strip(), value.strip()

        # Check if value starts with a quote.
        if len(value) > 0 and value[0] in '\'"':
            # Safer to evaluate as data-type than to remove quotes
            value = literal_eval(value)
        yield (key, value)
