import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from env.environment import StudentAcademicDayEnv
from env.policies import heuristic_policy


def evaluate(task):
    env = StudentAcademicDayEnv(task)
    obs = env.reset()
    total = 0.0

    while not env.done:
        action = heuristic_policy(obs.current_email, obs.calendar)
        obs, reward, done, _ = env.step(action)
        total += reward.value

    normalized = total / len(env.emails)
    return round(min(normalized, 1.0), 2)


if __name__ == "__main__":
    for task in ["easy", "medium", "hard"]:
        print(f"{task}: {evaluate(task)}")