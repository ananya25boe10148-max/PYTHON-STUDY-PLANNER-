from task_manager import load_data
from datetime import datetime

def suggest_tasks():
    data = load_data()
    today = datetime.today()

    scored_tasks = []

    for task in data["tasks"]:
        deadline = datetime.strptime(task["deadline"], "%Y-%m-%d")
        days_left = (deadline - today).days

        score = task["priority"] * 2 - days_left
        scored_tasks.append((score, task))

    scored_tasks.sort(reverse=True)

    print("\nTop Study Suggestions:")
    for score, task in scored_tasks[:3]:
        print(f"- {task['name']} (Deadline: {task['deadline']})")
