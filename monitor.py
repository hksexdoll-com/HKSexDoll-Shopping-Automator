"""
Public Page Monitoring Demo

This script demonstrates a lightweight availability check
for publicly accessible web pages.

- No authentication required
- No private data accessed
- For educational and automation demo purposes only
"""

import requests
import time

def check_site_availability(url: str) -> str:
    print(f"[INFO] Checking public status for: {url}")
    try:
        response = requests.get(url, timeout=10)
        return f"Site status: {response.status_code}"
    except Exception as e:
        return f"Connection error: {e}"

if __name__ == "__main__":
    TARGET = "https://www.hksexdoll.com"
    print(check_site_availability(TARGET))
    time.sleep(1)
