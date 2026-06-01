import json
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from src.agent_core import run_agent

def main():
    print("Day 9 Task Agent (type 'exit' to quit)\n")
    while True:
        goal = input("Goal: ").strip()
        if goal.lower() in {"exit", "quit"}:
            break
        if not goal:
            print("Please enter a goal.\n")
            continue

        result = run_agent(goal, max_steps=8)
        print("\nResult:")
        print(json.dumps(result, indent=2))
        print()

if __name__ == "__main__":
    main()