"""Provider wrapper for OpenRouter's OpenAI-compatible API."""
from typing import Optional

import requests


class OpenRouterProvider:
    def __init__(self, api_key: Optional[str], model: str = "openrouter/auto"):
        self.api_key = api_key
        self.model = model or "openrouter/auto"
        self.endpoint = "https://openrouter.ai/api/v1/chat/completions"

    def generate(self, prompt: str) -> str:
        if not self.api_key:
            raise RuntimeError("OpenRouter API key not configured")
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        payload = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
        }
        resp = requests.post(self.endpoint, headers=headers, json=payload, timeout=60)
        resp.raise_for_status()
        data = resp.json()
        try:
            return data["choices"][0]["message"]["content"].strip()
        except Exception:
            return ""
