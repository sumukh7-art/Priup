"""Logging utility for the Priup package."""

import logging
import sys


def get_logger(name: str) -> logging.Logger:
    """Creates and configures a logger for the given name.

    Args:
        name: The name of the logger (typically __name__).

    Returns:
        A configured logging.Logger instance.
    """
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger
