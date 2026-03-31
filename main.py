from task_manager import add_task, view_tasks, delete_task
from scheduler import suggest_tasks
from tracker import log_study, view_stats

def menu():
    while True:
        print("\n===== VITyarthi Study Planner =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Get Study Suggestion")
        print("5. Log Study Session")
        print("6. View Study Stats")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            suggest_tasks()
        elif choice == "5":
            log_study()
        elif choice == "6":
            view_stats()
        elif choice == "7":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    menu()
