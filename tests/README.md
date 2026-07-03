# Test Suite Directory

This directory contains the automated test suites for the Priup project, including unit tests, integration tests, and mocks.

---

## Directory Layout

We organize tests based on the source modules:

```text
tests/
├── unit/
│   ├── scraper/         # Tests for network requests and DOM extraction
│   ├── processor/       # Tests for boilerplate removal and segmentation
│   ├── analyzer/        # Tests for semantic classification models
│   └── reporter/        # Tests for grading parameters and report templates
├── integration/         # Multi-module tests executing the full pipeline
└── mocks/               # Static HTML pages and mock policy JSONs
```

---

## Running Tests

### Node.js / Scraper Tests:
If using a Node.js test harness (like Jest or Vitest):
```bash
npm run test
```

### Python / NLP Pipeline Tests:
If using pytest for the Python backend:
```bash
# Enter virtual environment first
source .venv/bin/activate
# Run test suite
pytest
```

---

## Writing New Tests

To maintain code reliability, we require the following from contributors:
1. **Coverage:** Every new module, helper, or core function must have accompanying unit tests.
2. **Naming Conventions:** Python test files must be prefixed with `test_` (e.g. `test_processor.py`). Node.js test files must end with `.test.ts` (e.g. `scraper.test.ts`).
3. **Mocks:** Avoid making live network requests or external API calls inside test files. Use local mock html documents in the `tests/mocks` folder.
