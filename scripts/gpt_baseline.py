import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from openai import OpenAI
from env.environment import StudentAcademicDayEnv
from env.models import Action


SYSTEM_PROMPT = """You are an academic email triage agent.
Choose the next best action for the current email.
Valid actions: ignore, mark_important, extract_deadline, schedule.
Return ONLY the action name.
Prioritize urgent academic events, deadlines, exams, scholarships, and fee notices.
Avoid duplicate scheduling if the subject already exists in the calendar.
"""


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def gpt_policy(observation):
    email = observation.current_email
    calendar_titles = [e.title for e in observation.calendar]

    prompt = f"""
Current email:
Subject: {email.subject}
Body: {email.body}
Sender: {email.sender}

Existing calendar titles: {calendar_titles}
Processed count: {observation.processed_count}

Choose exactly one action.
"""

    response = client.chat.completions.create(
        model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"),
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ],
        temperature=0,
    )

    action_name = response.choices[0].message.content.strip()
    return Action(action_type=action_name)


def evaluate(task="hard"):
    env = StudentAcademicDayEnv(task)
    obs = env.reset()
    total = 0.0

    while not env.done:
        action = gpt_policy(obs)
        obs, reward, done, info = env.step(action)
        total += reward.value

    return round(total, 2)


if __name__ == "__main__":
    for task in ["easy", "medium", "hard"]:
        print(f"GPT {task}: {evaluate(task)}")