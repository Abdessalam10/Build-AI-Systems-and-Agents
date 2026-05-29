# Building AI Systems — Agents

Minimal example agent harness demonstrating OpenAI function-calling and local tools.

## Prerequisites
- Python 3.10+
- An OpenAI API key set in a `.env` file as `OPENAI_API_KEY`.

## Install
Install dependencies:

```bash
pip install -r requirements.txt
```

## Quick start (CLI)
Run the interactive agent CLI which prompts for a goal and executes tool-based steps:

```bash
python scripts/agent_cli.py
```

Type a natural-language goal (for example: `List files in the workspace`) and the agent will attempt to satisfy it using the available tools.

## Notes
- Tool schemas live in `src/agent_core.py` and map model function calls to implementations in `src/tools.py`.
- Keep `max_steps` small during development to limit API calls.

