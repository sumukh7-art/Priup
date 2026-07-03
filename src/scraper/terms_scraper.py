"""Scraper module for extracting webpage HTML, text, and policy links."""

import re
from typing import Dict, Optional
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

from src.scraper.robots import can_fetch
from src.utils.logger import get_logger

logger = get_logger(__name__)


class TermsScraper:
    """Scraper to download webpages and extract terms/privacy policy URLs and text."""

    def __init__(
        self,
        user_agent: str = "PriupBot/0.1.0-alpha (+https://github.com/MrSpideyNihal/Priup)",
        timeout: int = 15,
    ):
        """Initializes the scraper with a user agent and request timeout.

        Args:
            user_agent: The User-Agent header value.
            timeout: The connection/read timeout in seconds.
        """
        self.headers = {"User-Agent": user_agent}
        self.timeout = timeout

    def fetch_page(self, url: str) -> Optional[requests.Response]:
        """Downloads a webpage, following redirects.

        Args:
            url: The URL of the webpage to download.

        Returns:
            The requests.Response object if successful.

        Raises:
            PermissionError: If robots.txt disallows fetching the URL.
            requests.RequestException: If the HTTP request fails.
        """
        logger.info(f"Checking robot permission for: {url}")
        if not can_fetch(url, self.headers["User-Agent"]):
            logger.warning(f"Crawling is disallowed by robots.txt for: {url}")
            raise PermissionError(f"Robots.txt disallows fetching {url}")

        try:
            logger.info(f"Fetching URL: {url}")
            response = requests.get(
                url,
                headers=self.headers,
                timeout=self.timeout,
                allow_redirects=True,
            )
            response.raise_for_status()
            return response
        except requests.RequestException as e:
            logger.error(f"Error fetching {url}: {e}")
            raise

    def find_policy_links(self, html_content: str, base_url: str) -> Dict[str, str]:
        """Scans the page HTML to find potential links to Privacy Policy and Terms of Service.

        Args:
            html_content: The HTML source of the page.
            base_url: The base URL of the page to resolve relative links.

        Returns:
            A dictionary containing detected keys ('privacy_policy', 'terms_conditions')
            and their absolute URLs if found.
        """
        soup = BeautifulSoup(html_content, "html.parser")
        links: Dict[str, str] = {}

        privacy_keywords = [
            r"privacy\s*policy",
            r"privacy",
            r"privacy\s*notice",
            r"data\s*policy",
            r"data\s*protection",
            r"cookie\s*policy",
        ]
        terms_keywords = [
            r"terms\s*of\s*service",
            r"terms\s*of\s*use",
            r"terms",
            r"terms\s*and\s*conditions",
            r"terms\s*&\s*conditions",
            r"legal\s*notice",
            r"user\s*agreement",
        ]

        privacy_patterns = [
            re.compile(kw, re.IGNORECASE) for kw in privacy_keywords
        ]
        terms_patterns = [
            re.compile(kw, re.IGNORECASE) for kw in terms_keywords
        ]

        for link in soup.find_all("a", href=True):
            href = link["href"].strip()
            text = link.get_text().strip()
            if not href:
                continue

            absolute_url = urljoin(base_url, href)

            # Match text or href
            for pattern in privacy_patterns:
                if pattern.search(text) or pattern.search(href):
                    if "privacy_policy" not in links:
                        links["privacy_policy"] = absolute_url
                        logger.info(
                            f"Found potential Privacy Policy link: {absolute_url}"
                        )
                    break

            for pattern in terms_patterns:
                if pattern.search(text) or pattern.search(href):
                    if "terms_conditions" not in links:
                        links["terms_conditions"] = absolute_url
                        logger.info(
                            f"Found potential Terms & Conditions link: {absolute_url}"
                        )
                    break

        return links

    def scrape_url(self, url: str) -> Dict[str, str]:
        """Fetches the target URL, extracts text/HTML, and finds legal policy links if it is a landing page.

        Args:
            url: The target website URL.

        Returns:
            A dictionary with keys: 'url', 'html', 'text', 'privacy_policy',
            'terms_conditions'.
        """
        response = self.fetch_page(url)
        if not response:
            raise ValueError(f"Failed to fetch content from {url}")

        final_url = response.url
        html_content = response.text

        # Extract basic text
        soup = BeautifulSoup(html_content, "html.parser")
        # Remove script and style elements
        for script in soup(["script", "style"]):
            script.decompose()
        text = soup.get_text(separator="\n")
        # clean text lines
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        clean_text = "\n".join(chunk for chunk in chunks if chunk)

        links = self.find_policy_links(html_content, final_url)

        return {
            "url": final_url,
            "html": html_content,
            "text": clean_text,
            "privacy_policy": links.get("privacy_policy", ""),
            "terms_conditions": links.get("terms_conditions", ""),
        }
