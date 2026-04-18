from pathlib import Path

import requests
import json

EMOJI_BASE_URL = "https://cdn.jsdelivr.net/npm/emojibase-data@17.0.0/en/data.json"
EMOJI_BASE_PATH = Path(__file__).parent.parent.parent / "data" / "emoji_base.json"

def download_emojibase():
    """Download the emojibase dataset from the internet and save it to the local file system."""
    response = requests.get(EMOJI_BASE_URL)
    response.raise_for_status()
    with open(EMOJI_BASE_PATH, "w", encoding="utf-8") as file:
        json.dump(response.json(), file, ensure_ascii=False, indent=2)


def get_emojibase() -> Path:
    """Retrieve the JSON emojibase dataset as a pathlib Path.

    Returns:
        Path: The path to the emojibase dataset JSON file.
    """
    if not EMOJI_BASE_PATH.exists():
        download_emojibase()
    return EMOJI_BASE_PATH


__all__ = ["download_emojibase", "get_emojibase"]
