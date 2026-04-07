# 🎓 Student Academic Day OpenEnv

A **real-world OpenEnv benchmark** where an AI agent helps a university student manage academic emails, detect urgent deadlines, extract room/time changes, avoid duplicate reminders, and build a clean academic calendar.

This benchmark simulates a realistic daily student workflow:
- email triage
- deadline extraction
- exam room changes
- duplicate prevention
- scheduling
- academic planning

---

# 🚀 Why this environment
This project is designed for the **OpenEnv Hackathon**.

It represents a real-world workflow humans actually perform:
> managing university emails, assignments, deadlines, and scheduling.

This makes it ideal for:
- agent benchmarking
- reward shaping experiments
- curriculum learning
- academic assistant agents
- long-horizon workflow planning

---

# 🧠 OpenEnv API
The environment follows the standard OpenEnv API:

```python
reset() -> Observation
state() -> Observation
step(action) -> observation, reward, done, info

Typed Pydantic models:
Observation
Action
Reward

📦 Observation Space
Each observation contains:
current unread email
remaining unread count
extracted entities
current calendar
action history
processed email count
Example:
Python
{
  "unread_count": 4,
  "current_email": {...},
  "calendar": [...],
  "processed_count": 2
}

🎯 Action Space
The agent performs one compound atomic action per email:
Python
Action(
    ignore=False,
    mark_important=True,
    extract_deadline=True,
    schedule=True
)
Supported fields:
ignore
mark_important
extract_deadline
schedule

🏆 Task Curriculum
The environment includes 3 difficulty levels.
- Easy⭐ 
2 emails:
    spam filtering
    single assignment deadline
- Medium⭐⭐ 
5 emails:
    multiple assignments
    internship deadline
    scholarship renewal
    noise filtering
- Hard⭐⭐⭐ 
10 emails:
    exam moved
    room change
    duplicate reminders
    fee payment
    lab slot conflicts
    multiple same-day deadlines

🎯 Reward Design
Dense reward shaping over the full trajectory.
Step-level rewards
spam correctly ignored → +0.2
important email detected → +0.25
deadline extracted → +0.25
scheduling successful → +0.3
duplicate scheduling penalty → -0.2
Episode-level grader
Final deterministic grader:
important deadlines preserved
duplicates removed
critical exam events scheduled
final score normalized to 0.0–1.0

🧪 Run Locally
Install
Bash
pip install -r requirements.txt

-_-Run baseline
Bash
python scripts/baseline.py

_-_Run GPT baseline
Windows PowerShell
PowerShell
$env:OPENAI_API_KEY="your_key"
python scripts/gpt_baseline.py
Run UI demo
Bash
python app.py
Open:
Plain text
http://localhost:7860

🐳 Docker
Benchmark baseline container
Bash
docker build -f Dockerfile.baseline -t student-openenv-baseline .
docker run student-openenv-baseline
Hugging Face Space container
Bash
docker build -t student-openenv-space .
docker run -p 7860:7860 student-openenv-space

✅ OpenEnv Validation
Bash
openenv validate

🤗 Hugging Face Deployment
Bash
huggingface-cli login
openenv push --repo-id YOUR_USERNAME/student-academic-openenv

📊 Expected Baseline Scores
Typical heuristic baseline:
Plain text
easy   ≈ 0.8–1.0
medium ≈ 0.7–0.9
hard   ≈ 0.6–0.8
GPT baseline typically performs higher on:
room changes
duplicate reminders
exam movement resolution

📁 Project Structure
Plain text
student-academic-openenv/
├── openenv.yaml
├── app.py
├── Dockerfile
├── Dockerfile.baseline
├── README.md
├── requirements.txt
├── env/
│   ├── __init__.py
│   ├── models.py
│   ├── parser.py
│   ├── tasks.py
│   ├── grader.py
│   ├── policies.py
│   └── environment.py
└── scripts/
    ├── baseline.py
    └── gpt_baseline.py