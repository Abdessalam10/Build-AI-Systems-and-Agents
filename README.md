Building AI Systems — Agents

A compact example repository demonstrating an agent-style AI harness built on OpenAI function-calling, local tooling, and small evaluation utilities. It includes:

- An interactive CLI agent that can call local tools (list/read/write/search files, calculator).
- A FastAPI-based conversational service for rapid testing and demoing.
- A set of workflow steps that extract structured information from free text and generate draft replies.
- A lightweight evaluation harness for validating model output against a JSON schema.

**Status:** Educational/sample code. Not production hardened. Use API keys and data responsibly.
Certificate
![Certificate](certif.jpg)
**Contents (high level)**

- `scripts/agent_cli.py` — Interactive CLI to run the agent.
- `src/agent_core.py` — Agent orchestration and tool schemas.
- `src/tools.py` — Local tool implementations (file ops, search, calc).
- `src/workflow_steps.py` — Example multi-step pipeline (extraction, routing, reply generation).
- `src/app.py` — FastAPI app exposing a simple chat endpoint.
- `scripts/eval_run.py` and `src/eval/validators.py` — Small evaluation harness for validating model JSON output.
- `tests/test_cases.json` — Example cases used by the evaluator.

Prerequisites

- Python 3.10 or newer
- An OpenAI API key. Set it in a `.env` file at the repository root, for example:

```bash
OPENAI_API_KEY=sk-...your-key...
```

Installation

1. Create and activate a virtual environment (recommended):

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

Quick usage

- Interactive agent CLI

```bash
python scripts/agent_cli.py
```

- Run the web demo (FastAPI)

```bash
uvicorn src.app:app --reload --port 8000
# then open http://127.0.0.1:8000/ or the /web static UI
```

- Run the evaluation harness

```bash
python scripts/eval_run.py
```

This will read `tests/test_cases.json` and validate model outputs according to `src/eval/validators.py`, saving a report to `reports/eval_report.json`.

Notes about running

- All code that calls OpenAI requires a valid `OPENAI_API_KEY` in the environment (the code uses `python-dotenv` to load from `.env`).
- The agent uses `src/agent_core.py` and a set of local tools implemented in `src/tools.py`. Adjust `max_steps` when testing to limit API calls.
- `scripts/eval_run.py` expects a function that returns the raw JSON (or serializable) output; by default it calls `src.workflow_steps.step2_extract_structured` and serializes its result for validation.

Project structure

See the repository root for full layout. Key files and folders:

- `scripts/` — convenience entrypoints and utilities
- `src/` — application and agent code
- `src/eval/` — validator and evaluation helpers
- `tests/` — sample test cases used by the evaluator
- `data/`, `prompts/`, `docs/` — example inputs and prompt templates

Contributing

- This repository is intended as a learning / demo resource. Feel free to open issues or PRs to improve examples, add tests, or harden safety checks.

License

No license file is included. If you intend to reuse this code in other projects, add a suitable license.

Questions / next steps

- If you want, I can:
	- run `python -m pip install -r requirements.txt` in this workspace (you must confirm),
	- patch `scripts/eval_run.py` to gracefully handle missing OpenAI keys when running offline, or
	- add a minimal `README` section that documents the evaluator's JSON schema precisely.


