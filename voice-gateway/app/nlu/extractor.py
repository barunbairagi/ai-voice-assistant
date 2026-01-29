import json
import os
from openai import OpenAI
from .schemas import IntentResult, AppointmentEntities
from .prompts import INTENT_EXTRACTION_PROMPT
from .rules import detect_intent_by_rules
from dotenv import load_dotenv
import re

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def clean_llm_json(raw: str) -> str:
    raw = raw.strip()

    # Remove ```json ... ``` or ``` ... ```
    if raw.startswith("```"):
        raw = re.sub(r"^```(?:json)?\s*", "", raw)
        raw = re.sub(r"\s*```$", "", raw)
    print(f"raw.strip(): {raw.strip()}")
    return raw.strip()
def extract_intent_and_entities(utterance: str) -> IntentResult:
    print("Started extract_intent_and_entities")
    # 2️⃣ Ask LLM for full extraction
    prompt = INTENT_EXTRACTION_PROMPT.format(utterance=utterance)

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    raw = response.choices[0].message.content
    fine_tune_data = clean_llm_json(raw)
    data = json.loads(fine_tune_data)
    print(f"Data from LLM:  {data}")
    return IntentResult(
        intent=data["intent"],
        entities=AppointmentEntities(**data["entities"])
    )
