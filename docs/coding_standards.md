# Coding Standards and Guidelines

This document outlines the coding standards, formatting guidelines, and architectural style rules for the Priup project. Following these standards keeps the codebase clean, readable, and maintainable.

---

## General Design Principles

1. **Keep it Modular:** Write small, reusable functions and classes that do one thing well.
2. **Handle Errors Gracefully:** Never let exceptions fail silently. Use try-catch blocks, log errors, and provide clear error messages.
3. **Write Self-Documenting Code:** Use clear, descriptive names for variables, functions, and classes. Avoid abbreviations.
4. **Test Your Changes:** All code changes must be accompanied by relevant unit or integration tests.

---

## Python Style Guide

We adhere to standard Python patterns to ensure readability and maintainability.

### 1. Style & Formatting
- **PEP 8 Compliance:** All Python code must comply with PEP 8.
- **Formatter:** We use **Black** for code formatting.
- **Linter:** We use **Ruff** or **Flake8** for linting.
- **Line Length:** Capped at 88 characters (Black default).

### 2. Type Hinting
All functions and methods must use type hints for parameter and return definitions:
```python
from typing import List, Dict, Any

def clean_paragraphs(paragraphs: List[str]) -> List[str]:
    cleaned: List[str] = []
    for text in paragraphs:
        stripped = text.strip()
        if stripped:
            cleaned.append(stripped)
    return cleaned
```

### 3. Naming Conventions
- **Modules and Packages:** `snake_case` (e.g. `text_processor.py`)
- **Classes:** `PascalCase` (e.g. `DocumentProcessor`)
- **Functions & Methods:** `snake_case` (e.g. `extract_policy_text`)
- **Variables & Constants:** `snake_case` for variables, `UPPER_SNAKE_CASE` for constants.

### 4. Docstrings
We use **Google-style** docstrings. Include docstrings for all modules, classes, and public functions:
```python
def classify_clause(clause_text: str) -> str:
    """Classifies a legal clause into a standard category.

    Args:
        clause_text: The raw text string of the clause.

    Returns:
        A string representing the classification category (e.g. 'Data Collection').
    """
```

---

## TypeScript / JavaScript Style Guide

Our TypeScript and frontend code follows modern ECMA standards.

### 1. Style & Formatting
- **Formatter:** **Prettier** with the following options:
  - Single quotes (`singleQuote: true`)
  - Semicolons (`semi: true`)
  - Tab width (`tabWidth: 2`)
  - Trailing commas (`trailingComma: 'es5'`)
- **Linter:** **ESLint** with standard TypeScript rules.
- **Type Safety:** Enable `strict` mode in `tsconfig.json`. Avoid using `any` types; prefer interfaces or explicit types.

### 2. Naming Conventions
- **Directories and Files:** `kebab-case` (e.g. `html-extractor.ts`)
- **Classes & Interfaces:** `PascalCase` (e.g. `HtmlExtractor`, `ScrapedDocument`)
- **Functions, Methods, & Variables:** `camelCase` (e.g. `scrapeUrl`, `rawHtml`)
- **Constants:** `UPPER_SNAKE_CASE` (e.g. `DEFAULT_TIMEOUT_MS`)

### 3. JSDoc
Use JSDoc block comments for functions and classes:
```typescript
/**
 * Scrapes raw HTML and text content from a URL.
 * 
 * @param url - The target webpage URL.
 * @param timeoutMs - Max wait time in milliseconds.
 * @returns The parsed HTML metadata and raw body text.
 */
async function scrapePage(url: string, timeoutMs: number): Promise<ScrapeResult> {
  // Implementation
}
```
