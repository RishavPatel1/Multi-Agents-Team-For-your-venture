"""Simple JSON-based persistence for the multi-agent system.

The module provides two helper functions:
    * ``load_state(path)`` – returns a dict mapping role -> saved history.
    * ``save_state(path, state_dict)`` – writes the dict to ``path``.

Each agent's ``dump_state`` / ``load_state`` methods are used to populate the
state dict.
"""

import json
from pathlib import Path
from typing import Dict, Any


def load_state(file_path: str) -> Dict[str, Any]:
    p = Path(file_path)
    if not p.exists():
        return {}
    return json.loads(p.read_text(encoding="utf-8"))


def save_state(file_path: str, state: Dict[str, Any]) -> None:
    p = Path(file_path)
    p.write_text(json.dumps(state, indent=2), encoding="utf-8")
