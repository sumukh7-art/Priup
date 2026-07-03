# Architectural Blueprint

This document details the system design, core modules, and technology stack for the Priup project. It serves as a technical reference for contributors working on the codebase.

---

## Architecture Overview

Priup is built as a modular pipeline where each step transforms the legal documents of a website into cleaner, more structured, and annotated representations, eventually producing a simplified report.

```
+-------------+      +---------------+      +--------------+      +--------------+
|             | Raw  |               | Clean |              | Tags |              |
|   Scraper   |----->|   Processor   |-----> |   Analyzer   |----->|   Reporter   |
|   Module    | HTML |    Module     | Text  |    Module    | Risk |    Module    |
|             |      |               |       |              |      |              |
+-------------+      +---------------+      +--------------+      +--------------+
       ^                                                                  |
       |                                                                  v
  [User URL]                                                        [JSON / UI]
```

---

## Component Details

### 1. Scraper Module (src/scraper)
* **Responsibility:** Retrieve raw text and HTML content from a target URL.
* **Requirements:**
  * Support for static websites (using high-speed HTTP clients like Axios or raw fetches).
  * Support for Single Page Applications (using headless browser controllers like Playwright or Puppeteer).
  * URL detection: Automatic discovery of "Privacy Policy" or "Terms of Service" links on the home page.
* **Output Format:**
  ```json
  {
    "url": "https://example.com/privacy",
    "scraped_at": "2026-07-03T12:00:00Z",
    "raw_html": "<html>...</html>",
    "headers": { ... }
  }
  ```

### 2. Processor Module (src/processor)
* **Responsibility:** Extract, clean, and segment the relevant text from raw HTML content.
* **Requirements:**
  * Boilerplate removal: Strip scripts, styles, headers, footers, and cookie popups.
  * Structural formatting: Retain structural hierarchies (headers, lists, tables).
  * Sentence segmentation: Divide the document into paragraphs and sentences.
* **Output Format:**
  ```json
  {
    "url": "https://example.com/privacy",
    "metadata": {
      "title": "Privacy Policy",
      "version": "Effective Jan 2026"
    },
    "paragraphs": [
      {
        "id": 1,
        "section": "Data Collection",
        "text": "We collect your email address when you sign up."
      }
    ]
  }
  ```

### 3. Analyzer Module (src/analyzer)
* **Responsibility:** Evaluate paragraph semantics and classify risks.
* **Requirements:**
  * Clause classification: Label clauses into categories (e.g., Collection, Sharing, Retention, Cookies).
  * Risk scoring: Tag clauses with risk levels (Low, Medium, High) based on predefined weights.
* **Output Format:**
  ```json
  {
    "url": "https://example.com/privacy",
    "clauses": [
      {
        "paragraph_id": 1,
        "category": "Data Collection",
        "risk_level": "Low",
        "risk_justification": "Standard email collection for account authentication.",
        "text": "We collect your email address when you sign up."
      }
    ]
  }
  ```

### 4. Reporter Module (src/reporter)
* **Responsibility:** Aggregate analysis details into structured summaries and scores.
* **Requirements:**
  * Score calculation: Aggregate risk levels into a total readability/privacy grade (e.g., A, B, C, D, F).
  * Summarization: Generate bulleted summaries for key categories.
* **Output Format:**
  ```json
  {
    "url": "https://example.com/privacy",
    "grade": "B",
    "overall_score": 85,
    "summary_bullets": [
      "Collects basic contact details for account setup (Low Risk).",
      "Shares cookies with third-party advertisers (Medium Risk)."
    ],
    "clauses": [...]
  }
  ```

---

## Technology Stack

The pipeline uses a multi-language stack to balance scraper performance, AI development, and integration capabilities:

- **Web Scraper & CLI Harness:** Node.js (TypeScript)
  * High-speed, event-driven network calls.
  * Node.js handles Playwright/Puppeteer rendering effectively.
- **AI Engine & NLP Processing:** Python (v3.10+)
  * Rich ecosystem for ML/AI (HuggingFace Transformers, spaCy, PyTorch).
  * Fast modeling and execution of embedding search / semantic models.
- **Summarization Engine:**
  * Primary: Local LLMs (using Ollama / Llama.cpp with Mistral or Llama-3-8B).
  * Cloud Fallback: Gemini API or OpenAI API integration.

---

## Security & Privacy Considerations

- **No User Data Storage:** Priup only processes public website URLs. The application does not store individual user histories or personal data.
- **Client-Side Option:** Provide developer configurations to run all AI processing locally via CPU/GPU, ensuring data privacy during text scans.
