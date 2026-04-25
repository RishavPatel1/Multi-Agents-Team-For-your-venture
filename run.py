"""Entry point for the multi-agent venture team.

Run with ``python -m multi_agent_team.run`` or ``python run.py`` from the
project root. The REPL supports:
    ask <role> <question>     – send a single question to a role
    broadcast <topic>          – send a message to all roles
    save                       – persist conversation history to ``state.json``
    load                       – restore persisted history
    roles                      – list available roles
    exit / quit                – leave the REPL
"""

import json
import sys
import os
from pathlib import Path

# Ensure the agents package can be imported when running this file directly.
# Adding the directory containing this script to ``sys.path`` makes absolute
# imports like ``agents.ceo`` work without requiring the project to be installed
# as a package.
script_dir = Path(__file__).parent
if str(script_dir) not in sys.path:
    sys.path.insert(0, str(script_dir))

# Import agent classes using absolute module names.
from agents.ceo import CEOAgent
from agents.cto import CTOAgent
from agents.developer import DeveloperAgent
from agents.hr import HRAgent
from agents.marketing import MarketingAgent
from agents.cfo import CFOAgent
from router import AgentRouter
from state import load_state, save_state

STATE_FILE = Path(__file__).parent / "state.json"

def build_router() -> AgentRouter:
    router = AgentRouter()
    router.register_agent("marketing", MarketingAgent())
    router.register_agent("cto", CTOAgent())
    router.register_agent("ceo", CEOAgent())
    router.register_agent("developer", DeveloperAgent())
    router.register_agent("hr", HRAgent())
    router.register_agent("cfo", CFOAgent())
    return router


def main() -> None:
    router = build_router()
    # Load any persisted state.
    persisted = load_state(str(STATE_FILE))
    for role, data in persisted.items():
        try:
            router._agents[role].load_state(data)
        except Exception:
            pass  # ignore corrupt entries

    print("Multi-Agent Venture Team REPL - type 'help' for commands.")
    while True:
        try:
            line = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting.")
            break
        if not line:
            continue
        parts = line.split(maxsplit=2)
        cmd = parts[0].lower()
        if cmd in {"exit", "quit"}:
            break
        if cmd == "help":
            print("Commands: ask <role> <question> | broadcast <msg> | save | load | roles | exit")
            continue
        if cmd == "roles":
            print("Available roles:", ", ".join(router.list_roles()))
            continue
        if cmd == "save":
            # Gather state from each agent.
            state = {role: agent.dump_state() for role, agent in router._agents.items()}
            save_state(str(STATE_FILE), state)
            print(f"State saved to {STATE_FILE}")
            continue
        if cmd == "load":
            persisted = load_state(str(STATE_FILE))
            for role, data in persisted.items():
                if role in router._agents:
                    router._agents[role].load_state(data)
            print("State loaded.")
            continue
        if cmd == "ask" and len(parts) >= 3:
            role = parts[1]
            question = parts[2]
            try:
                resp = router.send(role, question)
                print(resp)
            except Exception as e:
                print(f"Error: {e}")
            continue
        if cmd == "broadcast" and len(parts) >= 2:
            message = line[len("broadcast "):]
            resp = router.send("all", message)
            print(resp)
            continue
        print("Unrecognized command. Type 'help' for usage.")

if __name__ == "__main__":
    main()
