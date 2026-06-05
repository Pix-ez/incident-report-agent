# services/llm_service.py

import json
import os

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# client = OpenAI(
#     api_key=os.getenv("OPENAI_API_KEY")
# )


client = OpenAI(
    api_key=os.environ.get("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)


SYSTEM_PROMPT = """
You are a senior Site Reliability Engineer.

Analyze the incident evidence.

Determine:

1. Root cause
2. Confidence score (0-1)
3. Severity
4. Evidence summary
5. Recommended actions

Return valid JSON only.

{
  "root_cause": "",
  "confidence": 0.0,
  "severity": "",
  "evidence_summary": {},
  "recommendations": []
}
"""


def analyze_incident(context: dict):

    response = client.responses.create(
        model="openai/gpt-oss-120b",
        input=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": json.dumps(
                    context,
                    indent=2
                )
            }
        ]
    )

    return json.loads(
        response.output_text
    )