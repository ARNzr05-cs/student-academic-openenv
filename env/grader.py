from .parser import parse_email_entities


def grade_step(email, action, calendar, history):
    reward = 0.0
    entities = parse_email_entities(email.subject, email.body)
    event = None

    text = f"{email.subject} {email.body}".lower()
    important = any(k in text for k in ["due", "deadline", "exam", "urgent", "scholarship", "fee"])
    spam = any(k in text for k in ["club", "movie", "event", "open mic"])

    if spam and action.ignore:
        reward += 0.2

    if important:
        if action.mark_important:
            reward += 0.25
        if action.extract_deadline and entities:
            reward += 0.25
        if action.schedule:
            event = {
                "title": email.subject,
                "date": entities.get("deadline", "unknown"),
                "time": entities.get("time"),
                "room": entities.get("room"),
                "priority": 2,
            }
            reward += 0.3
            if any(e.title == event["title"] for e in calendar):
                reward -= 0.2

    reward += 0.1 if entities else 0.0
    reward = max(0.0, min(1.0, reward))
    return reward, "graded", entities, event


def final_grade(calendar, task_name):
    titles = [e.title for e in calendar]
    score = 0.0

    if task_name == "easy":
        score = min(len(titles) / 1.0, 1.0)
    elif task_name == "medium":
        score = min(len(set(titles)) / 4.0, 1.0)
    else:
        if "Networks exam" in titles:
            score += 0.3
        if "AI deadline" in titles:
            score += 0.2
        if "OS deadline" in titles:
            score += 0.2
        if len(titles) == len(set(titles)):
            score += 0.3

    return round(min(score, 1.0), 2)