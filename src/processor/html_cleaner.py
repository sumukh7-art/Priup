"""HTML Cleaning and processing module."""

import re
from typing import Any, Dict, List

from bs4 import BeautifulSoup

from src.utils.logger import get_logger

logger = get_logger(__name__)


class HTMLCleaner:
    """Processor to clean and parse HTML content, removing boilerplate."""

    def __init__(self):
        """Initializes HTMLCleaner with target tags to ignore."""
        self.ignored_tags = [
            "script",
            "style",
            "header",
            "footer",
            "nav",
            "aside",
            "iframe",
            "noscript",
            "svg",
            "button",
            "form",
            "input",
            "select",
            "textarea",
        ]

    def clean_html(self, html_content: str) -> str:
        """Strips scripts, styles, and other boilerplate elements from HTML.

        Args:
            html_content: The raw HTML string.

        Returns:
            A cleaned HTML string.
        """
        soup = BeautifulSoup(html_content, "html.parser")

        # Remove ignored tags
        for tag in self.ignored_tags:
            for element in soup.find_all(tag):
                element.decompose()

        # Remove elements by common cookie banner / popup class or id patterns
        popup_patterns = re.compile(
            r"cookie|consent|banner|popup|modal|overlay|gdpr", re.IGNORECASE
        )
        for element in soup.find_all(attrs={"class": popup_patterns}):
            element.decompose()
        for element in soup.find_all(attrs={"id": popup_patterns}):
            element.decompose()

        return str(soup)

    def extract_structured_paragraphs(self, html_content: str) -> List[Dict[str, Any]]:
        """Extracts structured text content grouped by section headings.

        Args:
            html_content: The cleaned HTML string.

        Returns:
            A list of dictionary objects representing structural paragraphs.
        """
        soup = BeautifulSoup(html_content, "html.parser")

        # Remove typical non-content elements if they weren't removed
        for tag in self.ignored_tags:
            for element in soup.find_all(tag):
                element.decompose()

        paragraphs: List[Dict[str, Any]] = []
        current_section = "General"
        paragraph_id = 1

        # We will iterate through block level elements
        content_elements = soup.find_all(
            ["h1", "h2", "h3", "h4", "h5", "h6", "p", "li"]
        )

        for element in content_elements:
            text = element.get_text().strip()
            if not text:
                continue

            # If it's a heading, update current section
            if element.name.startswith("h") or element.name.startswith("H"):
                current_section = text
                continue

            # Segment text into sentences if it's long
            sentences = self._segment_sentences(text)
            for sentence in sentences:
                paragraphs.append(
                    {
                        "id": paragraph_id,
                        "section": current_section,
                        "text": sentence,
                    }
                )
                paragraph_id += 1

        return paragraphs

    def _segment_sentences(self, text: str) -> List[str]:
        """Splits a paragraph block into individual sentences.

        Args:
            text: The paragraph text.

        Returns:
            A list of sentences.
        """
        # Simple regex split on sentence endings (. ! ?) followed by whitespace
        sentence_end = re.compile(r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s")
        sentences = sentence_end.split(text)
        return [s.strip() for s in sentences if s.strip()]
