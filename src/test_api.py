from pathlib import Path
import os

import requests
from dotenv import load_dotenv


# 프로젝트 최상위 폴더의 .env 파일 불러오기
PROJECT_ROOT = Path(__file__).resolve().parents[1]
load_dotenv(PROJECT_ROOT / ".env")

app_id = os.getenv("ADZUNA_APP_ID")
app_key = os.getenv("ADZUNA_APP_KEY")

# API 키가 제대로 저장되었는지 확인
if not app_id or not app_key:
    raise RuntimeError(
        "ADZUNA_APP_ID 또는 ADZUNA_APP_KEY를 .env 파일에서 찾을 수 없습니다."
    )

# 뉴욕의 Data Analyst 공고 5개 검색
url = "https://api.adzuna.com/v1/api/jobs/us/search/1"

params = {
    "app_id": app_id,
    "app_key": app_key,
    "results_per_page": 5,
    "what": "data analyst",
    "where": "New York",
}

response = requests.get(
    url,
    params=params,
    headers={"Accept": "application/json"},
    timeout=30,
)

response.raise_for_status()

data = response.json()
jobs = data.get("results", [])

print("API connection successful!")
print(f"Jobs returned: {len(jobs)}")
print()

for number, job in enumerate(jobs, start=1):
    company = job.get("company", {}).get(
        "display_name",
        "Unknown company",
    )
    location = job.get("location", {}).get(
        "display_name",
        "Unknown location",
    )

    print(f"{number}. {job.get('title', 'Unknown title')}")
    print(f"   Company: {company}")
    print(f"   Location: {location}")
    print()


