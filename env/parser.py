import re

MONTHS = r"(January|February|March|April|May|June|July|August|September|October|November|December)"


def parse_email_entities(subject: str, body: str):
    text = f"{subject} {body}"
    entities = {}

    date_match = re.search(rf"{MONTHS}\s\d{{1,2}}", text, re.IGNORECASE)
    if date_match:
        entities["deadline"] = date_match.group(0)

    time_match = re.search(r"\d{1,2}(?::\d{2})?\s?(AM|PM)", text, re.IGNORECASE)
    if time_match:
        entities["time"] = time_match.group(0)

    room_match = re.search(r"room\s([A-Z]\d+)", text, re.IGNORECASE)
    if room_match:
        entities["room"] = room_match.group(1)

    return entities