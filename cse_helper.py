import os
import requests
from dotenv import load_dotenv
import json

load_dotenv()

# 🔐 API Keys
GOOGLE_CSE_API_KEY = os.getenv("GOOGLE_CSE_API_KEY")
GOOGLE_CSE_CX = os.getenv("GOOGLE_CSE_CX")

def google_cse_search(query, num_results=5, debug=False):
    """
    Perform a Google Custom Search and extract LinkedIn profile links.
    """
    if not GOOGLE_CSE_API_KEY or not GOOGLE_CSE_CX:
        raise ValueError("Missing GOOGLE_CSE_API_KEY or GOOGLE_CSE_CX in environment variables.")

    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": GOOGLE_CSE_API_KEY,
        "cx": GOOGLE_CSE_CX,
        "q": query,
        "num": num_results,
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()

    if debug:
        print("🔍 DEBUG: Raw Google CSE response")
        print(json.dumps(data, indent=2))

    results = []
    for item in data.get("items", []):
        link = item.get("link", "")
        title = item.get("title", "")
        if "linkedin.com/in/" in link:
            name = title.split(" - ")[0].strip()
            results.append((name, link))

    if not results:
        fallback_url = f"https://www.google.com/search?q={query}"
        return [("Google Search Fallback", fallback_url)]

    return results[:num_results]
