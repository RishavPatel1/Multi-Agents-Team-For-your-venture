"""In-memory message router for the multi-agent team.

Usage
-----
    router = AgentRouter()
    router.register_agent("marketing", MarketingAgent())
    response = router.send("marketing", "How should we launch?")
"""

from __future__ import annotations

from typing import Dict

# Absolute import for BaseAgent when running the script directly.
from base_agent import BaseAgent


class AgentRouter:
    """Simple router that holds a mapping of role name → agent instance.
    It also supports broadcasting a message to *all* agents.
    """

    def __init__(self) -> None:
        self._agents: Dict[str, BaseAgent] = {}

    def register_agent(self, role: str, agent: BaseAgent) -> None:
        """Add a role agent to the router.
        ``role`` should be lower-case and unique.
        """
        self._agents[role.lower()] = agent

    def send(self, role: str, message: str) -> str:
        """Send *message* to the designated role and return its response.
        If ``role`` is ``"all"`` the method broadcasts the message to every
        registered agent and returns a JSON string mapping roles to their replies.
        """
        role_key = role.lower()
        if role_key == "all":
            results: Dict[str, str] = {}
            for r, agent in self._agents.items():
                results[r] = agent.process(message)
            # Return a nicely formatted representation.
            return "\n".join([f"[{r.upper()}] {resp}" for r, resp in results.items()])
        if role_key not in self._agents:
            raise ValueError(f"No agent registered for role '{role}'. Available: {list(self._agents)}")
        return self._agents[role_key].process(message)

    def list_roles(self) -> list[str]:
        return list(self._agents.keys())
