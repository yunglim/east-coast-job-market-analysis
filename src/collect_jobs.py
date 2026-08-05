from datetime import datetime, timezone
from pathlib import Path
import os
import time

import pandas as pd
import requests
from dotenv import load_dotenv


# ==================================================
# 1. Project folders and API credentials
# ==================================================

PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"

load_dotenv(PROJECT_ROOT / ".env")

APP_ID = os.getenv("ADZUNA_APP_ID")
APP_KEY = os.getenv("ADZUNA_APP_KEY")

if not APP_ID or not APP_KEY:
    raise RuntimeError(
        "ADZUNA_APP_ID or ADZUNA_APP_KEY was not found in the .env file."
    )


# ==================================================
# 2. Search settings
# ==================================================

LOCATIONS = {
    "NY": "New York",
    "NJ": "New Jersey",
    "DC": "Washington, DC",
    "VA": "Virginia",
    "MD": "Maryland",
}

SEARCH_TERMS = [
    "data analyst",
    "business intelligence analyst",
    "marketing analyst",
    "operations analyst",
    "reporting analyst",
]

RESULTS_PER_SEARCH = 20
API_URL = "https://api.adzuna.com/v1/api/jobs/us/search/1"


# ==================================================
# 3. Collect job postings
# ==================================================

session = requests.Session()
rows = []

for state_code, location_query in LOCATIONS.items():
    for search_term in SEARCH_TERMS:
        print(f"Collecting: {search_term} in {location_query}")

        params = {
            "app_id": APP_ID,
            "app_key": APP_KEY,
            "results_per_page": RESULTS_PER_SEARCH,
            "what": search_term,
            "where": location_query,
        }

        try:
            response = session.get(
                API_URL,
                params=params,
                headers={"Accept": "application/json"},
                timeout=30,
            )

            response.raise_for_status()

        except requests.RequestException as error:
            print(f"Request failed: {error}")
            print()
            continue

        response_data = response.json()
        results = response_data.get("results", [])

        print(f"  Jobs returned: {len(results)}")

        for job in results:
            company = job.get("company") or {}
            location = job.get("location") or {}
            category = job.get("category") or {}

            location_area = location.get("area") or []

            rows.append(
                {
                    "job_id": job.get("id"),
                    "title": job.get("title"),
                    "company": company.get("display_name"),
                    "location": location.get("display_name"),
                    "location_area": " | ".join(location_area),
                    "query_state": state_code,
                    "query_location": location_query,
                    "search_term": search_term,
                    "category": category.get("label"),
                    "description": job.get("description"),
                    "created": job.get("created"),
                    "salary_min": job.get("salary_min"),
                    "salary_max": job.get("salary_max"),
                    "contract_time": job.get("contract_time"),
                    "contract_type": job.get("contract_type"),
                    "latitude": job.get("latitude"),
                    "longitude": job.get("longitude"),
                    "job_url": job.get("redirect_url"),
                    "collected_at_utc": datetime.now(
                        timezone.utc
                    ).isoformat(),
                }
            )

        print()

        # Avoid sending requests too quickly
        time.sleep(0.5)


# ==================================================
# 4. Save raw data as CSV
# ==================================================

if not rows:
    raise RuntimeError(
        "No job postings were collected. Check the API connection and search settings."
    )

RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

jobs_df = pd.DataFrame(rows)

timestamp = datetime.now().strftime("%Y%m%d_%H%M")
output_path = RAW_DATA_DIR / f"adzuna_jobs_{timestamp}.csv"

jobs_df.to_csv(output_path, index=False)

print("=" * 50)
print("Collection complete!")
print(f"Rows collected: {len(jobs_df)}")
print(f"Unique job IDs: {jobs_df['job_id'].nunique()}")
print(
    f"Duplicate job IDs: "
    f"{jobs_df['job_id'].duplicated().sum()}"
)
print(f"CSV columns: {len(jobs_df.columns)}")
print(f"Saved to: {output_path}")
print("=" * 50)


