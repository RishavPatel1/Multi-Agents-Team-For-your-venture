"""Base class for all role agents.

Each agent implements a simple ``process`` method that forwards the
user's message to an LLM via the OpenRouter API (using ``httpx``) and returns the response.
"""

from __future__ import annotations

import os
import json
from pathlib import Path
from typing import Any, Dict, List

# Load environment variables from .env if present.
try:
    from dotenv import load_dotenv
    load_dotenv()
except Exception:
    pass

import httpx

# OpenRouter endpoint for chat completions.
_OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"
_OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
if not _OPENROUTER_API_KEY:
    raise RuntimeError("OPENROUTER_API_KEY not set – please add it to .env")


def _post_chat(messages: List[Dict[str, Any]]) -> Dict[str, Any]:
    headers = {
        "Authorization": f"Bearer {_OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://openrouter.ai",
        "X-Title": "Claude Multi-Agent Team",
    }
    payload = {
        # Use the user-requested OSS model.
        "model": "openai/gpt-oss-120b:free",
        "messages": messages,
        "temperature": 0.2,
        "max_tokens": 1024,
    }
    response = httpx.post(_OPENROUTER_API_URL, headers=headers, json=payload, timeout=60.0)
    response.raise_for_status()
    return response.json()


class BaseAgent:
    """Common functionality for role-specific agents.

    Parameters
    ----------
    name: str
        Human-readable role name (e.g., "Marketing").
    system_prompt: str
        The system prompt that defines the agent's persona and expertise.
    """

    def __init__(self, name: str, system_prompt: str) -> None:
        self.name = name
        self.system_prompt = system_prompt
        self._history: List[Dict[str, Any]] = []

    def _build_messages(self, user_message: str) -> List[Dict[str, Any]]:
        messages: List[Dict[str, Any]] = [{"role": "system", "content": self.system_prompt}]
        if self._history:
            messages.extend(self._history[-20:])
        messages.append({"role": "user", "content": user_message})
        return messages

    def process(self, message: str) -> str:
        messages = self._build_messages(message)
        response = _post_chat(messages)
        self._history.append({"role": "user", "content": message})
        reply = response["choices"][0]["message"]["content"]
        self._history.append({"role": "assistant", "content": reply})
        return reply

    def dump_state(self) -> Dict[str, Any]:
        return {"history": self._history}

    def load_state(self, data: Dict[str, Any]) -> None:
        self._history = data.get("history", [])
