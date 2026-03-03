# API Documentation

This document outlines the internal class structures and the external API dependencies used by the Metadata Audit system.

## External API Dependencies

### 1. CMS API
Used to retrieve the current list of ranked titles.
- **Endpoint:** `GET /v1/homepage/ranked-titles`
- **Response Schema:**
  ```json
  [
    {
      "title_id": "string",
      "rank": "integer",
      "content_type": "MOVIE | SHOW"
    }
  ]
  ```

### 2. Metadata Service
Used to validate the assets for a specific title.
- **Endpoint:** `GET /v1/metadata/{title_id}`
- **Response Schema:**
  ```json
  {
    "imdb_id": "string | null",
    "summary_text": "string | null",
    "asset_links": {
      "trailer": "string | null"
    }
  }
  ```

## Internal Components

### `AuditProcessor`
The main orchestrator for the audit flow.
- **`process_title(title_rank)`**: Asynchronously fetches metadata and runs the audit engine for a single title.
- **`run(output_path)`**: Executes the full pipeline: Fetch -> Audit -> Report.

### `AuditEngine`
Contains the business logic for metadata validation.
- **`audit(title_rank, metadata)`**: Compares the presence of fields and returns an `AuditResult`.
- **Logic Rules:**
    - **Complete:** Has IMDB ID and Trailer.
    - **Missing IMDB:** IMDB ID is null/empty.
    - **Missing Trailer:** Trailer URL is null/empty.
    - **Missing Both:** Both fields are null/empty.

### `ExcelReportWriter`
Handles the generation of the `.xlsx` file.
- **`generate(dataframe)`**: Filters data into "Movies" and "Shows" and writes them to separate sheets in a single workbook.
