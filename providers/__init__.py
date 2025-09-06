"""LLM provider factory."""
from .gemini_provider import GeminiProvider
from .ollama_provider import OllamaProvider
from .lmstudio_provider import LMStudioProvider
from .openrouter_provider import OpenRouterProvider


def get_provider(name: str, cfg: dict):
    name = name.lower()
    if name == "gemini":
        return GeminiProvider(cfg.get("api_key"))
    if name == "ollama":
        return OllamaProvider(cfg.get("endpoint"))
    if name == "lmstudio":
        return LMStudioProvider(cfg.get("endpoint"))
    if name == "openrouter":
        return OpenRouterProvider(cfg.get("api_key"), cfg.get("model"))
    raise ValueError(f"Unknown provider: {name}")
