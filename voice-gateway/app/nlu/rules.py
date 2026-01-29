def detect_intent_by_rules(text: str) -> str | None:
    t = text.lower()
    if "book" in t or "appointment" in t or "see a doctor" in t:
        return "book_appointment"
    if "cancel" in t:
        return "cancel_appointment"
    if "reschedule" in t or "change" in t:
        return "reschedule_appointment"
    if "human" in t or "operator" in t:
        return "handoff_human"
    return None
