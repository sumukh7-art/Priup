# Analyzer Module

This directory contains the AI, Natural Language Processing, and scoring models for the Priup project. Its primary responsibility is to analyze each paragraph of a privacy policy and terms of service, categorize it into distinct domain categories, and score the risk.

---

## Architectural Role

1. **Semantic Categorization:** Assigns each text paragraph to standard categories (e.g., Data Retention, Data Sharing, Cookie Usage, User Choice, Security Measures).
2. **Risk Identification:** Performs rule-based and model-based scanning of text to find terms of service/privacy risks.
3. **Risk Level Assignment:** Flags items as Low, Medium, or High Risk, providing a logical justification for each choice.

---

## Tech Stack Recommendations

- **Python (v3.10+):** Core backend language for AI modeling.
- **Classification Engines:**
  - **Sentence Transformers / Embeddings:** semantic search or cosine similarity against standard risk anchors.
  - **Supervised ML Models:** Using Scikit-Learn (SGDClassifier, SVM) or HuggingFace tokenizers/models fine-tuned on legal text datasets (like the [OPP-115 Dataset](https://usableprivacy.org/data)).
- **LLM Integration:** Using local models via **Ollama** (e.g., Mistral, Llama-3) or cloud LLM APIs (Gemini/OpenAI) for zero-shot semantic categorization and reasoning verification.

---

## Pipeline Integration

```
+--------------------+        +---------------------+        +--------------------+
| Segmented Document | ---->  | AI Scoring & ML     | ---->  | Annotated Document |
+--------------------+        +---------------------+        +--------------------+
                                                             (Passes to Reporter)
```

The analyzer outputs annotated clauses:
```python
from typing import List, TypedDict

class AnnotatedClause(TypedDict):
    paragraph_id: int
    text: str
    category: str              # e.g., "Data Retention"
    risk_level: str            # "Low", "Medium", or "High"
    risk_justification: str    # Why it's flagged as high/med risk (e.g. "States that data is stored forever")

class AnnotatedDocument(TypedDict):
    url: str
    clauses: List[AnnotatedClause]
```
