"""Simple HTML fetcher to obtain basic product context."""
import requests
from bs4 import BeautifulSoup


def fetch_product_context(url: str) -> str:
    """Fetch minimal product information from a URL."""
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")
        title = soup.title.string.strip() if soup.title else ""
        return f"Product page title: {title}" if title else ""
    except Exception:
        return ""
