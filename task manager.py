import json
from datetime import datetime

FILE = "data.json"

def load_data():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return {"tasks": [], "study": []}

def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_task():
    data = load_data()
    name = input("Task name: ")
    deadline = input("Deadline (YYYY-MM-DD): ")
    priority = int(input("Priority (1-5): "))

    data["tasks"].append({
        "name": name,
        "deadline": deadline,
        "priority": priority
    })

    save_data(data)
    print("Task added!")

def view_tasks():
    data = load_data()
    for i, task in enumerate(data["tasks"]):
        print(f"{i+1}. {task['name']} | Deadline: {task['deadline']} | Priority: {task['priority']}")

def delete_task():
    data = load_data()
    view_tasks()
    idx = int(input("Enter task number to delete: ")) - 1
    if 0 <= idx < len(data["tasks"]):
        data["tasks"].pop(idx)
        save_data(data)
        print("Deleted!")
