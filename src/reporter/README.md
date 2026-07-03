# Reporter Module

This directory contains the reporting, summarization, and grading models for the Priup project. Its primary responsibility is to compile annotated legal clauses into readable summaries and calculate an overall readability and privacy rating.

---

## Architectural Role

1. **Rating Calculation:** Aggregates individual clause risks using weighted scoring parameters to generate a final rating grade (e.g. A, B, C, D, F).
2. **Key Summary Generation:** Generates descriptive, human-readable bullet points summarizing findings for each major domain.
3. **Structured Export:** Emits structured JSON outputs for integrations (like browser extensions or API users) and creates markdown or HTML report cards.

---

## Tech Stack Recommendations

- **Python or TypeScript:** This layer acts as the output bridge. Both Node.js and Python are suitable depending on deployment requirements.
- **Text Summarization:** LLMs (Gemini, Mistral, or Llama-3) prompted to generate brief summaries of grouped legal clauses.
- **Reporting Outputs:**
  - JSON schema definitions.
  - Markdown-to-HTML engines (such as Marked or markdown-it) to render styled report cards.

---

## Pipeline Integration

```
+--------------------+        +---------------------+        +--------------------+
| Annotated Document | ---->  | Summaries & Grading | ---->  | Final Report JSON  |
+--------------------+        +---------------------+        +--------------------+
                                                             (Exposed to client)
```

The reporter outputs final summaries:
```json
{
  "url": "https://example.com/privacy",
  "grade": "C",
  "score": 62,
  "lastAnalyzed": "2026-07-03T12:00:00Z",
  "summary": {
    "positives": [
      "Explicit user consent is obtained before sharing data with third parties."
    ],
    "negatives": [
      "Retains user interaction logs indefinitely.",
      "Vague cookies clauses allow ad-network tracking."
    ]
  },
  "categories": {
    "dataRetention": {
      "score": 40,
      "summary": "Retains data indefinitely, failing to provide specific deletion dates."
    }
  }
}
```
