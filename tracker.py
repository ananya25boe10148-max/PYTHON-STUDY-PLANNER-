from task_manager import load_data, save_data
from datetime import datetime

def log_study():
    data = load_data()
    subject = input("Subject: ")
    hours = float(input("Hours studied: "))

    data["study"].append({
        "subject": subject,
        "hours": hours,
        "date": str(datetime.today().date())
    })

    save_data(data)
    print("Session logged!")

def view_stats():
    data = load_data()
    total = sum(s["hours"] for s in data["study"])
    print(f"\nTotal Study Hours: {total}")

    subjects = {}
    for s in data["study"]:
        subjects[s["subject"]] = subjects.get(s["subject"], 0) + s["hours"]

    for sub, hrs in subjects.items():
        print(f"{sub}: {hrs} hrs")
