# Priup Project Roadmap

This document outlines the vision, development phases, and future plans for Priup. As an early-stage open-source project, this roadmap serves as a guide for contributors to see where they can help.

---

## Vision
To build a free, transparent, and automated system that translates dense legal website documents (Privacy Policies and Terms & Conditions) into simple, searchable, and structured summaries with automated risk ratings. We want to empower users to know exactly what they are agreeing to in seconds.

---

## Development Phases

### Phase 1: Scraper & Text Processing (Active Planning)
The goal of this phase is to build robust mechanisms to extract raw text content from target URLs and prepare it for analysis.

- **Scraper Engine:**
  - Build a CLI scraper that accepts website URLs.
  - Implement fallback scrapers: high-speed static HTML parsing (e.g., BeautifulSoup/Cheerio) and dynamic browser rendering (e.g., Playwright/Puppeteer) for single-page applications.
  - Research robust methods to auto-detect and isolate links to privacy policy and terms documents on index pages.

- **Text Processing Pipeline:**
  - Remove boilerplate text, headers, footers, cookies notices, and navigation elements.
  - Standardize text format (UTF-8 normalization, whitespace cleaning).
  - Perform sentence segmentation and structure parsing (identifying sections, headers, and bullet points).

---

### Phase 2: AI/NLP Semantic Analysis
This phase transforms clean text into structured semantic sections, labeling sections by their domain (e.g., "Data Retention", "Third-Party Sharing").

- **Clause Classification:**
  - Develop or fine-tune text classification models (using platforms like HuggingFace, spaCy, or fastText) to label paragraphs.
  - Match clauses to standard privacy categories (e.g., Data Collection, User Tracking, Data Security, User Choice, Jurisdiction).

- **Risk Vector Extraction:**
  - Implement heuristic and NLP rule-based systems to scan for negative/positive patterns (e.g., "we sell your data", "we store logs indefinitely").
  - Categorize extracted clauses into three risk levels: Low, Medium, and High.

---

### Phase 3: Scoring & Summarization
In this phase, we aggregate risk tags into numeric ratings and generate short summaries of clauses.

- **Scoring Engine:**
  - Design a transparent scoring algorithm that aggregates risk scores across multiple dimensions.
  - Implement default scoring weights for each category (e.g., selling user data decreases the score significantly more than keeping logs for 30 days).

- **Summarization Pipeline:**
  - Build prompting templates and integrations for Large Language Models (LLMs) like Gemini, OpenAI, or local models (via Ollama/Llama.cpp) to summarize complex legal jargon into bullet points.
  - Construct automated summaries for each classification category.

---

### Phase 4: Integrations & Extensions
This phase focuses on getting the summaries and scores in front of users where they need them.

- **Web Browser Extension:**
  - Build a browser extension (Chrome, Firefox, Safari) that detects the current site's privacy rating on the fly.
  - Render simplified overlay summary cards when visiting a site.

- **Web Dashboard:**
  - Build a centralized directory of analyzed websites, allowing users to search, compare, and request analyses.
  - Provide a crowdsourced platform where users can verify AI-generated labels.

- **API Interface:**
  - Build a developer-friendly REST/gRPC API for programmatic checks of website privacy health.
