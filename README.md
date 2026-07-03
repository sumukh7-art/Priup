# Priup

<p align="center">
  <a href="https://github.com/MrSpideyNihal/Priup/actions"><img src="https://img.shields.io/github/actions/workflow/status/MrSpideyNihal/Priup/ci.yml?branch=main&label=CI&style=flat-square" alt="Build Status"></a>
  <a href="LICENSE"><img src="https://img.shields.io/github/license/MrSpideyNihal/Priup?style=flat-square&color=blue" alt="License"></a>
  <a href="https://github.com/MrSpideyNihal/Priup/pulls"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square" alt="PRs Welcome"></a>
  <a href="ROADMAP.md"><img src="https://img.shields.io/badge/status-planning-orange?style=flat-square" alt="Project Status"></a>
</p>

Priup is an open-source framework and application designed to help users demystify website Privacy Policies and Terms & Conditions. By combining robust web scraping, NLP cleaning, AI analysis, scoring, and automated summarization, Priup provides human-friendly reports highlighting risks, trackers, and rights.

> **Status:** The **first production-quality Python foundation** has been implemented, including a modular scraper (`src/scraper`) and HTML processing/cleaning pipelines (`src/processor`).

---

## Current Progress & Implemented Scraper

We have implemented the initial Python backend foundation under `src/`:
* **Scraper Module ([src/scraper](file:///C:/Users/ASUS/.gemini/antigravity/scratch/Priup/src/scraper)):** 
  - Downloads target web pages and follows HTTP redirects using `requests`.
  - Automatically parses and validates against the website's `robots.txt` using `robots.py` to ensure ethical crawling.
  - Automatically identifies potential Privacy Policy and Terms & Conditions links within the web page.
* **Processor Module ([src/processor](file:///C:/Users/ASUS/.gemini/antigravity/scratch/Priup/src/processor)):**
  - Cleans raw HTML boilerplate (removing scripts, styles, headers, footers, navigation tags, and cookie consent overlays) using `beautifulsoup4`.
  - Groups texts under structural headings and segments them into clean sentences.
* **Logger Utility ([src/utils](file:///C:/Users/ASUS/.gemini/antigravity/scratch/Priup/src/utils)):**
  - Standardized logger output format for tracking execution.
* **Examples ([examples/](file:///C:/Users/ASUS/.gemini/antigravity/scratch/Priup/examples)):**
  - An example script `examples/example_scrape.py` demonstrating end-to-end scraper and HTML cleaner execution.
* **Tests ([tests/](file:///C:/Users/ASUS/.gemini/antigravity/scratch/Priup/tests)):**
  - Unit tests verifying the terms scraper and cleaner modules with mocked HTTP requests.

---

---

## Architectural Workflow

The complete, end-to-end data pipeline of Priup operates as follows:

```
Website URL
     │
     ▼ [Scraper]
Extract Privacy Policy & Terms (raw HTML/text)
     │
     ▼ [Processor]
Clean & Process Text (NLP cleaning, sentence segmentation)
     │
     ▼ [Analyzer]
AI / NLP Analysis (semantic categorization & risk detection)
     │
     ▼ [Reporter]
Summarization & Scoring (risk weights and highlights)
     │
     ▼
Simple Human-Friendly Report (Score & summary cards)
```

For a detailed view of the system design and technology choices, read the [Architecture Documentation](docs/architecture.md).

---

## Project Structure

```text
Priup/
├── .github/                 # GitHub workflows & issue/PR templates
├── docs/                    # Architectural plans and guidelines
│   ├── architecture.md      # Detailed system design
│   ├── development.md       # Setup & environment guides
│   └── coding_standards.md  # Standard formatting & style rules
├── src/                     # Core source code
│   ├── scraper/             # Target webpage content extraction
│   ├── processor/           # Text sanitization, chunking, and metadata parsing
│   ├── analyzer/            # AI analysis, classification, and scoring
│   └── reporter/            # Summary generation and report building
├── tests/                   # Unit & integration tests
├── examples/                # Example scripts demonstrating CLI & library usage
├── CHANGELOG.md             # Release history
├── CODE_OF_CONDUCT.md       # Community guidelines
├── CONTRIBUTING.md          # Guide for developers & PR checklist
├── LICENSE                  # MIT License details
├── ROADMAP.md               # Future milestones & evolution plan
└── SECURITY.md              # Security policies & reporting channels
```

---

## Getting Started

### Prerequisites

To set up the development environment, make sure you have:
* **Node.js** (v18 or higher) for the scrapers/scaffolding
* **Python** (v3.10 or higher) for the core AI/NLP models

### Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/MrSpideyNihal/Priup.git
   cd Priup
   ```

2. **Backend (Python) Setup:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -r requirements.txt # once created
   ```

3. **Frontend / Tools (Node.js) Setup:**
   ```bash
   npm install
   ```

For detailed setup instructions and env configurations, check [docs/development.md](docs/development.md).

---

## Roadmap

We are progressing through several development stages:

1. **Phase 1: Scraping & Text Processing** (Extraction engines and cleaning pipelines)
2. **Phase 2: Semantic Analysis & Risk Modeling** (Classification of legal clauses)
3. **Phase 3: Scoring & Summarization** (Scoring engine & LLM summary templates)
4. **Phase 4: Extension & User Reports** (Chrome Extension and web app interface)

Read [ROADMAP.md](ROADMAP.md) to learn how to contribute to current milestones.

---

## Contributing

We welcome contributions from developers, UI/UX designers, privacy lawyers, and writers!
* Read [CONTRIBUTING.md](CONTRIBUTING.md) to understand our branching, issue flow, and PR guidelines.
* Follow our code format guidelines in [docs/coding_standards.md](docs/coding_standards.md).
* Keep standard behaviors in check using the [Code of Conduct](CODE_OF_CONDUCT.md).

---

## License

Priup is open-source and licensed under the [MIT License](LICENSE).
