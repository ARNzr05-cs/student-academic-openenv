import gradio as gr
from env.environment import StudentAcademicDayEnv
from env.policies import heuristic_policy


def run_demo(task_name):
    env = StudentAcademicDayEnv(task_name)
    obs = env.reset()

    logs = []
    total = 0.0

    while not env.done:
        email = obs.current_email
        logs.append(f"EMAIL → {email.subject}")

        action = heuristic_policy(email, obs.calendar)

        obs, reward, done, info = env.step(action)
        total += reward.value

        logs.append(
            f"  ACTION → ignore={action.ignore}, "
            f"important={action.mark_important}, "
            f"extract={action.extract_deadline}, "
            f"schedule={action.schedule} "
            f"| reward={reward.value:.2f}"
        )

        if info.get("entities"):
            logs.append(f"  ENTITIES → {info['entities']}")

    normalized = round(min(total / len(env.emails), 1.0), 2)

    board = [[
        task_name,
        normalized,
        len(obs.calendar),
        obs.processed_count
    ]]

    return "\n".join(logs), board


with gr.Blocks() as demo:
    gr.Markdown("# 🎓 Student Academic Day OpenEnv")

    task = gr.Dropdown(
        ["easy", "medium", "hard"],
        value="hard",
        label="Task Difficulty"
    )

    btn = gr.Button("Run Benchmark")

    out = gr.Textbox(
        lines=20,
        label="Execution Logs"
    )

    board = gr.Dataframe(
        headers=["Task", "Score", "Events", "Processed"],
        label="Scoreboard"
    )

    btn.click(
        run_demo,
        inputs=task,
        outputs=[out, board]
    )


if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
