from .models import Observation, Reward, CalendarEvent, Email
from .tasks import get_task
from .grader import grade_step, final_grade


class StudentAcademicDayEnv:
    def __init__(self, task_name="hard"):
        self.task_name = task_name
        self.reset()

    def reset(self):
        task = get_task(self.task_name)
        self.emails = [Email(**e) for e in task["emails"]]
        self.index = 0
        self.calendar = []
        self.history = []
        self.done = False
        return self.state()

    def state(self):
        current = self.emails[min(self.index, len(self.emails) - 1)]
        return Observation(
            unread_count=max(0, len(self.emails) - self.index),
            current_email=current,
            calendar=self.calendar,
            extracted_entities={},
            processed_count=self.index,
            history=self.history,
        )

    def step(self, action):
        if self.done:
            return self.state(), Reward(value=0.0, reason="done"), True, {}

        email = self.emails[self.index]
        value, reason, entities, event = grade_step(email, action, self.calendar, self.history)

        if event and not any(e.title == event["title"] for e in self.calendar):
            self.calendar.append(CalendarEvent(**event))

        self.history.append(email.subject)
        self.index += 1

        if self.index >= len(self.emails):
            self.done = True
            value += final_grade(self.calendar, self.task_name)
            value = min(value, 1.0)

        return self.state(), Reward(value=value, reason=reason), self.done, {"entities": entities}