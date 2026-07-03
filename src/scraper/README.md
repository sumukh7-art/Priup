# Scraper Module

This directory contains the web scraping engine for the Priup project. Its primary responsibility is to retrieve the raw HTML or text content from a target privacy policy or terms and conditions URL.

---

## Architectural Role

1. **URL Input:** Receives a target URL or crawls an index page to discover privacy/terms links.
2. **Dynamic Rendering Support:** Headless browser automation to scrape Single Page Applications (SPAs) where content is injected dynamically via client-side JavaScript.
3. **Static Fetch Support:** Rapid static HTTP fetches when JavaScript rendering is not required.
4. **Data Delivery:** Outputs raw scraped documents to the `src/processor` pipeline.

---

## Tech Stack Recommendations

- **Node.js / TypeScript:** We recommend using TypeScript for the scraper layer because of the rich headless browser ecosystem.
- **Headless Browser:** [Playwright](https://playwright.dev/) or [Puppeteer](https://pptr.dev/). Playwright is preferred for its robust multi-browser support and automatic waits.
- **HTTP Client (Static):** Axios or built-in `fetch` for quick static requests.
- **HTML Parser (Static):** [Cheerio](https://cheerio.js.org/) for loading and querying static HTML DOM structures.

---

## Pipeline Integration

```
+------------+        +-------------------+        +---------------+
| Target URL | ---->  | Scraper Execution | ---->  | Raw JSON File |
+------------+        +-------------------+        +---------------+
                                                   (Passes to Processor)
```

The scraper outputs raw webpage content structured as follows:
```typescript
interface ScrapedDocument {
  url: string;
  scrapedAt: string; // ISO timestamp
  status: number;    // HTTP response status
  rawHtml: string;   // Entire document body
  headers: Record<string, string>;
}
```
