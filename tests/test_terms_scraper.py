"""Unit tests for the TermsScraper and HTMLCleaner classes."""

import unittest
from unittest.mock import MagicMock, patch

import requests

from src.processor.html_cleaner import HTMLCleaner
from src.scraper.terms_scraper import TermsScraper


class TestTermsScraper(unittest.TestCase):
    """Test suite for the TermsScraper class."""

    @patch("src.scraper.terms_scraper.can_fetch")
    @patch("requests.get")
    def test_fetch_page_success(self, mock_get, mock_can_fetch):
        """Verifies that fetch_page downloads a webpage and respects headers."""
        # Arrange
        mock_can_fetch.return_value = True
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.url = "https://example.com"
        mock_response.text = "<html><body>Test</body></html>"
        mock_get.return_value = mock_response

        scraper = TermsScraper()

        # Act
        response = scraper.fetch_page("https://example.com")

        # Assert
        self.assertIsNotNone(response)
        self.assertEqual(response.text, "<html><body>Test</body></html>")
        mock_get.assert_called_once_with(
            "https://example.com",
            headers=scraper.headers,
            timeout=scraper.timeout,
            allow_redirects=True,
        )

    @patch("src.scraper.terms_scraper.can_fetch")
    def test_fetch_page_disallowed_by_robots(self, mock_can_fetch):
        """Verifies that fetch_page raises PermissionError when disallowed by robots.txt."""
        # Arrange
        mock_can_fetch.return_value = False
        scraper = TermsScraper()

        # Act & Assert
        with self.assertRaises(PermissionError):
            scraper.fetch_page("https://example.com")

    def test_find_policy_links(self):
        """Verifies detection of Privacy Policy and Terms of Service links in HTML."""
        # Arrange
        html = """
        <html>
            <body>
                <a href="/privacy-policy">Privacy Policy</a>
                <a href="https://example.com/terms">Terms of Service</a>
                <a href="/about">About Us</a>
            </body>
        </html>
        """
        scraper = TermsScraper()

        # Act
        links = scraper.find_policy_links(html, "https://example.com")

        # Assert
        self.assertEqual(
            links.get("privacy_policy"), "https://example.com/privacy-policy"
        )
        self.assertEqual(links.get("terms_conditions"), "https://example.com/terms")


class TestHTMLCleaner(unittest.TestCase):
    """Test suite for the HTMLCleaner class."""

    def test_clean_html(self):
        """Verifies boilerplate tags and cookie banners are stripped."""
        # Arrange
        html = """
        <html>
            <head><style>body { color: red; }</style></head>
            <body>
                <header><h1>My Header</h1></header>
                <div class="cookie-banner">Accept cookies</div>
                <main>
                    <p>Main content text.</p>
                </main>
                <footer>Footer content</footer>
                <script>console.log("hello");</script>
            </body>
        </html>
        """
        cleaner = HTMLCleaner()

        # Act
        cleaned = cleaner.clean_html(html)

        # Assert
        self.assertNotIn("My Header", cleaned)
        self.assertNotIn("cookie-banner", cleaned)
        self.assertNotIn("console.log", cleaned)
        self.assertIn("Main content text.", cleaned)

    def test_extract_structured_paragraphs(self):
        """Verifies paragraphs are structured by section and split into sentences."""
        # Arrange
        html = """
        <html>
            <body>
                <h2>Introduction</h2>
                <p>This is the first sentence. This is the second sentence.</p>
                <h2>Data Collection</h2>
                <p>We collect your email.</p>
            </body>
        </html>
        """
        cleaner = HTMLCleaner()

        # Act
        paragraphs = cleaner.extract_structured_paragraphs(html)

        # Assert
        self.assertEqual(len(paragraphs), 3)
        self.assertEqual(paragraphs[0]["section"], "Introduction")
        self.assertEqual(paragraphs[0]["text"], "This is the first sentence.")
        self.assertEqual(paragraphs[1]["text"], "This is the second sentence.")
        self.assertEqual(paragraphs[2]["section"], "Data Collection")
        self.assertEqual(paragraphs[2]["text"], "We collect your email.")


if __name__ == "__main__":
    unittest.main()
