"""Provider wrapper for local Ollama server."""
from typing import Optional

import requests


class OllamaProvider:
    def __init__(self, endpoint: Optional[str]):
        self.endpoint = endpoint

    def generate(self, prompt: str) -> str:
        if not self.endpoint:
            raise RuntimeError("Ollama endpoint not configured")
        payload = {"prompt": prompt}
        resp = requests.post(self.endpoint, json=payload, timeout=60)
        resp.raise_for_status()
        data = resp.json()
        return data.get("response") or data.get("output", "")
