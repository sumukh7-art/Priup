"""Scraper module package."""

from src.scraper.robots import can_fetch
from src.scraper.terms_scraper import TermsScraper

__all__ = ["TermsScraper", "can_fetch"]
