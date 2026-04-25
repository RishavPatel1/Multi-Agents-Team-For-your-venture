"""CFOAgent – loads the CFO prompt and uses BaseAgent."""

from pathlib import Path
import json

# Absolute import for BaseAgent when running the script directly.
from base_agent import BaseAgent


def _load_prompt() -> str:
    prompt_path = Path(__file__).parent.parent / "prompts" / "cfo.json"
    data = json.loads(prompt_path.read_text(encoding="utf-8"))
    return data["prompt"]


class CFOAgent(BaseAgent):
    def __init__(self) -> None:
        super().__init__(name="CFO", system_prompt=_load_prompt())
