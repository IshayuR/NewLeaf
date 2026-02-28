import html
import os
import re
import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()


def _get_secret(key: str) -> str | None:
    try:
        return st.secrets[key]
    except (KeyError, FileNotFoundError):
        return os.getenv(key)


def _clean_html(text: str) -> str:
    text = html.unescape(text)
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

FALLBACK_JOBS = [
    {
        "title": "Warehouse Associate",
        "company": "QuickShip Logistics",
        "location": "Your Area",
        "description": "Entry-level warehouse position. Duties include sorting packages, loading trucks, and keeping the workspace clean. No experience needed — training provided.",
        "url": "https://www.indeed.com/q-warehouse-associate-jobs.html",
        "salary": "$15–$18/hr",
    },
    {
        "title": "Kitchen Helper",
        "company": "Golden Plate Catering",
        "location": "Your Area",
        "description": "Help prep meals, wash dishes, and keep the kitchen organized. Great first step into the food-service industry. Meals included during shifts.",
        "url": "https://www.indeed.com/q-kitchen-helper-jobs.html",
        "salary": "$14–$16/hr",
    },
    {
        "title": "Janitorial / Cleaning Crew",
        "company": "BrightSpace Facility Services",
        "location": "Your Area",
        "description": "Evening and weekend cleaning shifts at office buildings. Supplies and training provided. Reliable transportation helpful but not required.",
        "url": "https://www.indeed.com/q-janitorial-jobs.html",
        "salary": "$13–$15/hr",
    },
]


def fetch_jobs(zip_code: str, keywords: str) -> list[dict]:
    app_id = _get_secret("ADZUNA_APP_ID")
    app_key = _get_secret("ADZUNA_API_KEY")

    if not app_id or not app_key:
        return FALLBACK_JOBS

    try:
        params = {
            "app_id": app_id,
            "app_key": app_key,
            "where": zip_code,
            "what": f"{keywords} entry level",
            "results_per_page": 10,
            "sort_by": "date",
            "distance": 25,
        }
        resp = requests.get(
            "https://api.adzuna.com/v1/api/jobs/us/search/1",
            params=params,
            timeout=10,
        )
        resp.raise_for_status()
        data = resp.json()

        jobs = []
        for item in data.get("results", []):
            salary_min = item.get("salary_min")
            salary_max = item.get("salary_max")
            salary = None
            if salary_min and salary_max:
                salary = f"${int(salary_min):,}–${int(salary_max):,}/yr"
            elif salary_min:
                salary = f"From ${int(salary_min):,}/yr"

            clean_title = _clean_html(item.get("title", "Job Opening"))
            clean_desc = _clean_html(item.get("description", ""))[:200]

            jobs.append(
                {
                    "title": clean_title,
                    "company": item.get("company", {}).get("display_name", "Company"),
                    "location": item.get("location", {}).get("display_name", ""),
                    "description": clean_desc,
                    "url": item.get("redirect_url", "#"),
                    "salary": salary,
                }
            )
        return jobs if jobs else FALLBACK_JOBS

    except Exception:
        return FALLBACK_JOBS
