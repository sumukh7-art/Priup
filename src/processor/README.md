# Processor Module

This directory contains the text cleaning, sanitization, and segmentation pipeline for the Priup project. Its primary responsibility is to parse raw web markup, extract meaningful policy text, and segment it into structured chunks for AI analysis.

---

## Architectural Role

1. **Boilerplate Stripping:** Remove HTML tags, styles, scripts, cookie banners, navigation lists, headers, and footers.
2. **Text Normalization:** Clean character encodings, normalize whitespaces, and decode HTML entities.
3. **Structure Retention:** Preserve header levels (H1, H2, H3), list structures, and table organizations.
4. **Sentence & Paragraph Segmentation:** Split the document into individual clean paragraphs and indexable sentences for targeted semantic classification.

---

## Tech Stack Recommendations

- **Python (v3.10+):** Python is recommended for this module because of its rich ecosystem of HTML cleanup tools and natural language processing libraries.
- **HTML Extraction:** 
  - [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) for fine-grained DOM parsing.
  - [Trafilatura](https://trafilatura.readthedocs.io/) or [Readability-lxml](https://github.com/buriy/python-readability) for high-quality main text extraction.
- **NLP Segmentation:** [spaCy](https://spacy.io/) (using the sentencizer component) or [NLTK](https://www.nltk.org/) (using the Punkt tokenizer) for reliable sentence boundary detection.

---

## Pipeline Integration

```
+---------------+        +---------------------+        +--------------------+
| Scraped HTML  | ---->  | Extraction Pipeline | ---->  | Segmented Document |
+---------------+        +---------------------+        +--------------------+
                                                        (Passes to Analyzer)
```

The processor outputs cleaned document schemas:
```python
from typing import List, Dict, TypedDict

class Paragraph(TypedDict):
    id: int
    header_context: List[str] # Hierarchical parent headers (e.g., ["Data Protection", "Third-Party Sharing"])
    text: str

class CleanedDocument(TypedDict):
    url: str
    metadata: Dict[str, str]  # Page titles, update dates, etc.
    paragraphs: List[Paragraph]
```
