from .models import Action

TRUSTED_SENDERS = {"admin@uni.edu", "ai@uni.edu", "finance@uni.edu", "aid@uni.edu"}


def heuristic_policy(email, calendar=None):
    calendar = calendar or []
    text = f"{email.subject} {email.body}".lower()

    if any(e.title == email.subject for e in calendar):
        return Action(ignore=True)

    important = (
        email.sender in TRUSTED_SENDERS
        or any(k in text for k in ["exam", "due", "deadline", "scholarship", "fee"])
    )

    if important:
        return Action(
            mark_important=True,
            extract_deadline=True,
            schedule=True,
        )

    return Action(ignore=True)