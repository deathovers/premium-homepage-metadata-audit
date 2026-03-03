# User Guide: Metadata Audit Report

## Introduction
The Metadata Audit Report is a daily tool used by Content Operations to ensure that all titles promoted on the Premium Homepage have the necessary information for a high-quality user experience.

## Understanding the Report
The generated Excel file contains two tabs: **Movies** and **Shows**.

### Column Definitions
- **Rank:** The position of the title on the homepage (1 is the top spot).
- **Title Name:** The display name of the content.
- **IMDB ID:** Displays the ID or "MISSING".
- **Trailer URL:** Displays the link or "MISSING".
- **Summary Status:** `True` if a summary exists, `False` if not.
- **Audit Status:** 
    - `Complete`: All assets present.
    - `Missing IMDB`: Needs an IMDB ID update.
    - `Missing Trailer`: Needs a trailer link.
    - `Missing Both`: Critical metadata missing.

## Gap Analysis (Action Required)
The primary focus for the operations team should be titles where:
1. **Summary Status** is `True`.
2. **Audit Status** is NOT `Complete`.

These titles represent "Gaps" where the user can read about the content but cannot see a trailer or view IMDB ratings, leading to a poor experience.

## Troubleshooting
- **Report is empty:** Ensure the CMS API is reachable and returning ranked titles.
- **"Error" in Audit Status:** This indicates a timeout or connection failure for that specific title during the audit. The system will retry 3 times before marking it as an error.
- **Missing Titles:** Only titles currently ranked on the "Premium Homepage" are included in this report.
