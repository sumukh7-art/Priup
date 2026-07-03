#!/usr/bin/env python
"""Example script demonstrating usage of the Priup scraper and processor foundation."""

import json
import os
import sys

# Add parent directory to path to enable importing from src
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.processor.html_cleaner import HTMLCleaner
from src.scraper.terms_scraper import TermsScraper
from src.utils.logger import get_logger

logger = get_logger("example_scrape")


def main():
    """Main execution of the scraping example."""
    target_url = "https://example.com"
    logger.info(f"Starting example scrape for {target_url}")

    scraper = TermsScraper()
    cleaner = HTMLCleaner()

    try:
        # Step 1: Scrape target URL
        result = scraper.scrape_url(target_url)
        logger.info("Successfully scraped the page.")
        logger.info(f"Final URL: {result['url']}")
        logger.info(f"Detected Privacy Policy link: {result['privacy_policy']}")
        logger.info(f"Detected Terms & Conditions link: {result['terms_conditions']}")

        # Step 2: Clean and parse the HTML
        cleaned_html = cleaner.clean_html(result["html"])
        logger.info("Successfully cleaned HTML boilerplate.")

        # Step 3: Extract structured paragraphs
        paragraphs = cleaner.extract_structured_paragraphs(cleaned_html)
        logger.info(
            f"Extracted {len(paragraphs)} structured sentences/paragraphs."
        )

        # Print the first few paragraphs
        logger.info("Sample of extracted paragraphs:")
        print(json.dumps(paragraphs[:5], indent=2))

    except Exception as e:
        logger.error(f"Failed to execute example scraping: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
