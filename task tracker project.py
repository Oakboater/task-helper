import json
import os
# Task tracker

# SAVE THE TASKS THROUGH A JSON FILE

#REQUIREMENTS




def task():
    while True:
        try:
            askuser = input(
                "Welcome User how may I help you today?\n"
                "1. Add task\n"
                "2. Update task\n"
                "3. Delete task\n"
                "4. List Undone tasks\n"
                "5. List done tasks\n"
            )
        except ValueError:
            print("Invalid input. Please try again.")
            return
        
        if askuser == "1":
            try:
                asktask = input("What task are you adding?")
                data = {"tasks": [asktask]}  # Create a dictionary with the new task
                with open('data.json', 'a') as f:
                    json.dump(data, f)
            except ValueError:
                print("Invalid input. Please try again.")



        if askuser == "2":
            try:
                with open('data.json', 'r') as f:
                    data = json.load(f)
                    print(data.get("tasks", []))
                    taskinput = input("What would you like to edit?")
                    if taskinput in data:
                        with open('data.json', 'a') as f:
                            tasks = data.get("tasks", [])
                            if taskinput in tasks:
                                idx = tasks.index(taskinput)
                                tasks[idx] = f"{taskinput} (completed)"
                                data["tasks"] = tasks
                                with open('data.json', 'w') as fw:
                                    json.dump(data, fw)
                            else:
                                print("Task not found.")

            except FileNotFoundError:
             print("data.json file not found.")


        if askuser == "3":
            try:
                with open('data.json', 'r') as f:
                    data = json.load(f)
                tasks = data.get("tasks", [])
                print("Current tasks:", tasks)
                taskdelete = input("Enter the exact task you want to delete: ")
                if taskdelete in tasks:
                    tasks.remove(taskdelete)
                    data["tasks"] = tasks
                    with open('data.json', 'w') as fw:
                        json.dump(data, fw, indent=4)
                    print(f"Task '{taskdelete}' deleted.")
                else:
                    print("Task not found.")
            except FileNotFoundError:
                print("data.json file not found.")
            except Exception as e:
                print(f"An error occurred: {e}")


        if askuser == "4":
            delist()


        if askuser == "5":
            alllist()
        



 # Remove or modify this as needed



#Mark a task as in progress or done
#List all tasks that are done
#List all tasks that are not done
# List all tasks that are in progress
if __name__ in "__main__":
    task()
