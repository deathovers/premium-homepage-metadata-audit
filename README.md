# Automated Premium Homepage Metadata Audit

## Project Overview
The **Automated Premium Homepage Metadata Audit** is a specialized tool designed to monitor the quality and completeness of content metadata for titles featured on the "Premium Homepage." 

The system identifies titles that are currently ranked but are missing critical assets—specifically **IMDB IDs** and **Trailer URLs**—with a particular focus on "Gaps" where a content summary exists but the associated assets do not.

## Key Features
- **Automated Retrieval:** Fetches real-time ranking data from the CMS.
- **Metadata Validation:** Cross-references titles with the Metadata Service to verify IMDB IDs, Summaries, and Trailer assets.
- **Gap Analysis:** High-priority flagging for titles that have summaries but are missing assets.
- **Categorized Reporting:** Generates a dual-tab Excel report separating "Movies" and "Shows."
- **High Performance:** Utilizes asynchronous processing with `asyncio` and `httpx` to handle up to 500 titles in under 5 minutes.
- **Resilience:** Built-in exponential backoff retries for API stability.

## Architecture
The system follows a modular architecture:
1. **API Clients:** `CMSClient` and `MetadataClient` handle external communication.
2. **Audit Engine:** Pure logic component that determines the status of a title based on metadata rules.
3. **Audit Processor:** The orchestrator that manages concurrency, rate limiting, and the data pipeline.
4. **Excel Writer:** Data transformation layer using `pandas` to generate the final report.

## Installation

### Prerequisites
- Python 3.9+
- Access to CMS and Metadata Service APIs

### Setup
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure environment variables (see [Configuration](#configuration)).

## Usage
To run a manual audit:
```bash
python main.py --output report_$(date +%F).xlsx
```

## Configuration
The system can be configured via environment variables or a `.env` file:
- `CMS_API_URL`: Base URL for the CMS service.
- `METADATA_API_URL`: Base URL for the Metadata service.
- `CONCURRENCY_LIMIT`: Maximum number of simultaneous API requests (default: 10).
- `RETRY_COUNT`: Number of retries for failed API calls (default: 3).
