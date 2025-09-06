"""Provider wrapper for Google's Gemini models."""
from typing import Optional

import google.generativeai as genai


class GeminiProvider:
    def __init__(self, api_key: Optional[str]):
        self.api_key = api_key
        if api_key:
            genai.configure(api_key=api_key)
            self.model = genai.GenerativeModel("gemini-pro")
        else:
            self.model = None

    def generate(self, prompt: str) -> str:
        if not self.model:
            raise RuntimeError("Gemini API key not configured")
        response = self.model.generate_content(prompt)
        return getattr(response, "text", "")
