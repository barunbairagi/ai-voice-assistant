from fastapi import FastAPI
from app.nlu.extractor import extract_intent_and_entities
from app.nlu.dialogue.manager import decide_next_question, get_prompt_for_slot

app = FastAPI()

@app.post("/voice/webhook")
def voice_webhook(payload: dict):
    transcript = payload["transcript"]

    nlu_result = extract_intent_and_entities(transcript)

    next_slot = decide_next_question(nlu_result.intent, nlu_result.entities)

    if next_slot:
        prompt = get_prompt_for_slot(next_slot)
        return {"say": prompt}

    return {"say": "Thank you. Your appointment details are complete."}
