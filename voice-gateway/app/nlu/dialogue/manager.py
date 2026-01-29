REQUIRED_SLOTS = {
    "book_appointment": [
        "patient_name",
        "visit_reason",
        "appointment_date",
        "appointment_time"
    ]
}


def decide_next_question(intent: str, entities):
    required = REQUIRED_SLOTS.get(intent, [])

    for slot in required:
        if getattr(entities, slot) is None:
            return slot

    return None


def get_prompt_for_slot(slot: str) -> str:
    prompts = {
        "patient_name": "May I have your full name please?",
        "visit_reason": "What is the reason for your visit?",
        "appointment_date": "Which date would you like the appointment?",
        "appointment_time": "What time works best for you?"
    }
    return prompts.get(slot, "Could you please clarify?")
