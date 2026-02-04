import requests
import time

def check_updates(url: str) -> str:
    print(f"[INFO] Checking public status for: {url}")
    try:
        response = requests.get(url, timeout=10)
        return f"Site status: {response.status_code}"
    except Exception as e:
        return f"Connection error: {e}"

if __name__ == "__main__":
    TARGET = "https://www.hksexdoll.com"
    print(check_updates(TARGET))
    time.sleep(1)
