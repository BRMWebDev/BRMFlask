"""Utilities: Logging utility."""
import logging
import coloredlogs


def make_logger(name="__name__"):
    """Instantiate the logger."""
    coloredlogs.install()
    log = logging.getLogger(name)
    # out_handler = logging.StreamHandler(sys.stdout)
    # log.addHandler(out_handler)
    return log

log = make_logger()
