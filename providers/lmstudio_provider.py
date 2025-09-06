"""Provider wrapper for LM Studio's OpenAI-compatible endpoint."""
from typing import Optional

import requests


class LMStudioProvider:
    def __init__(self, endpoint: Optional[str]):
        self.endpoint = endpoint

    def generate(self, prompt: str) -> str:
        if not self.endpoint:
            raise RuntimeError("LM Studio endpoint not configured")
        payload = {
            "model": "default",
            "messages": [{"role": "user", "content": prompt}],
        }
        resp = requests.post(self.endpoint, json=payload, timeout=60)
        resp.raise_for_status()
        data = resp.json()
        try:
            return data["choices"][0]["message"]["content"].strip()
        except Exception:
            return ""
