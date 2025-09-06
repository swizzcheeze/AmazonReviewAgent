import json
import os

CONFIG_FILE = "config.json"

DEFAULT_CONFIG = {
    "pipeline": {
        "writer_provider": "gemini",
        "editor_provider": "lmstudio",
    },
    "providers": {
        "gemini": {"api_key": "YOUR_API_KEY_HERE"},
        "ollama": {"endpoint": "http://localhost:11434/api/generate"},
        "lmstudio": {"endpoint": "http://localhost:1234/v1/chat/completions"},
        "openrouter": {"api_key": "YOUR_API_KEY_HERE", "model": "openrouter/auto"},
    },
}


def load_config():
    """Load configuration from disk, creating default if missing."""
    if not os.path.exists(CONFIG_FILE):
        save_config(DEFAULT_CONFIG)
    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_config(cfg: dict) -> None:
    """Persist configuration to disk."""
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(cfg, f, indent=2)
