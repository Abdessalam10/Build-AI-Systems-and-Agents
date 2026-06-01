import json
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
	sys.path.insert(0, str(ROOT_DIR))

from src.ai_json_function import analyze_text_to_validated_json

text = "Subject: Urgent password reset required. Click http://fake-link.example now."
result = analyze_text_to_validated_json(text)

print(json.dumps(result, indent=2))