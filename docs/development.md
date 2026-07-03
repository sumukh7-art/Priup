# Local Development Setup Guide

This guide describes how to configure, run, and test your local Priup development environment.

---

## System Prerequisites

Verify that the following runtimes are installed on your development machine:
* **Python (3.10 or higher):** Required for the NLP pipeline, models, and processors.
* **Node.js (18.x LTS or higher):** Required for the scrapers, web app, and build tooling.
* **Git:** For source control management.

---

## Step-by-Step Installation

### 1. Repository Setup
Clone the repository and enter the directory:
```bash
git clone https://github.com/MrSpideyNihal/Priup.git
cd Priup
```

### 2. Backend (Python) Configuration
We recommend using a Python virtual environment to isolate project dependencies.

#### Windows:
```powershell
python -m venv .venv
.venv\Scripts\activate
```

#### macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

#### Installing Packages:
Update pip and install dependencies (both standard and development tools):
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install -r requirements-dev.txt
```
*(Note: If these files are not present yet during the planning phase, you can manually run `pip install pytest black flake8 ruff` inside the environment).*

### 3. Scraping & Scaffolding (Node.js) Configuration
Install Node packages and tools:
```bash
npm install
```

---

## Environment Configuration

Copy the sample environment file to create your local configurations:
```bash
cp .env.example .env
```

Open `.env` in your editor and configure variables as needed:
```ini
# Environment settings
NODE_ENV=development
LOG_LEVEL=info

# Scraper configurations
SCRAPER_TIMEOUT_MS=30000
USER_AGENT="PriupBot/0.1.0-alpha (+https://github.com/MrSpideyNihal/Priup)"

# AI & LLM Engine configurations
LLM_PROVIDER=ollama # Options: ollama, gemini, openai
LLM_MODEL=mistral
OLLAMA_HOST=http://localhost:11434

# API Keys (if using cloud providers)
GEMINI_API_KEY=your_gemini_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
```

---

## Verifying Setup

Ensure your local installation works by executing linters and placeholders:

### Linting Node/TypeScript Files:
```bash
npm run lint --if-present
```

### Linting Python Files:
```bash
# Run Ruff check
ruff check .
# Run Black code formatter check
black --check .
```

### Running Test Harnesses:
```bash
# Run Node/TS tests
npm test --if-present

# Run Python tests
pytest
```
