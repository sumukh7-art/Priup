"""Robots.txt parser and validator for ethical scraping."""

import urllib.robotparser
from typing import Dict
from urllib.parse import urljoin, urlparse

import requests

from src.utils.logger import get_logger

logger = get_logger(__name__)

# Cache robot parsers per base URL to avoid fetching robots.txt repeatedly
_robots_cache: Dict[str, urllib.robotparser.RobotFileParser] = {}


def can_fetch(url: str, user_agent: str = "*") -> bool:
    """Checks if a URL can be fetched according to the site's robots.txt.

    Args:
        url: The target URL to check.
        user_agent: The User-Agent string to check against.

    Returns:
        True if the URL is allowed to be fetched, False otherwise.
    """
    try:
        parsed_url = urlparse(url)
        if not parsed_url.netloc:
            return False

        base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
        robots_url = urljoin(base_url, "/robots.txt")

        if base_url not in _robots_cache:
            rp = urllib.robotparser.RobotFileParser()
            rp.set_url(robots_url)
            try:
                headers = {"User-Agent": user_agent}
                response = requests.get(robots_url, headers=headers, timeout=5)
                if response.status_code == 404:
                    # If robots.txt doesn't exist, we assume crawling is allowed
                    rp.parse([])
                else:
                    rp.parse(response.text.splitlines())
            except requests.RequestException as e:
                logger.warning(
                    f"Could not retrieve robots.txt from {robots_url}: {e}. "
                    "Defaulting to allowing crawl."
                )
                rp.parse([])
            _robots_cache[base_url] = rp

        return _robots_cache[base_url].can_fetch(user_agent, url)
    except Exception as e:
        logger.warning(
            f"Error checking robots.txt for {url}: {e}. Defaulting to True."
        )
        return True
