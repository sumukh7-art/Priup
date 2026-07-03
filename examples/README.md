# Examples Directory

This directory contains example scripts, CLI execution configurations, and integration samples showing developers how to use and embed Priup components in their own applications.

---

## Directory Contents

- **`cli_demo.py` / `cli_demo.ts`:** (Placeholder) Simple scripts demonstrating how to execute the full scrape-to-report pipeline from the command line.
- **`custom_weights.py`:** (Placeholder) Demonstrates how to load the analyzer and configure custom scoring weights for privacy evaluations.
- **`batch_analyzer.py`:** (Placeholder) Sample script showcasing how to scan a list of URLs in parallel and export reports in CSV/JSON formats.

---

## Running Examples

Before running examples, ensure your local development environment is configured and dependencies are installed. See [docs/development.md](../docs/development.md).

### Running Python Examples:
Make sure your virtual environment is active:
```bash
source .venv/bin/activate # Or .venv\Scripts\activate on Windows
python examples/cli_demo.py --url "https://example.com/privacy"
```

### Running TypeScript/Node Examples:
Ensure packages are compiled or run directly via ts-node:
```bash
npx ts-node examples/cli_demo.ts --url "https://example.com/privacy"
```
