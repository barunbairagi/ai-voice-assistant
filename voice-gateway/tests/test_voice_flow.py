import pytest
from app.nlu.dialogue.manager import decide_next_question, get_prompt_for_slot
from app.nlu.schemas import AppointmentEntities, IntentResult
from app.nlu.extractor import extract_intent_and_entities

def test_extract_intent():
    transcript="Hi, I am Rahul, I want to see a skin dosctor tomorrow morning."

    nlu_result = extract_intent_and_entities(transcript)

    next_slot = decide_next_question(nlu_result.intent, nlu_result.entities)

    if next_slot:
        prompt = get_prompt_for_slot(next_slot)
        print(f"say: {prompt}")
    else:
        print(f"say: Thank you. Your appointment details are complete.")
