from data import tasks

def add_task(tasks,task_id,task_to_do,status):
    for task in tasks:
        if task["id"]==task_id:
            print("Task already exist! with this id..")
            return
    task_data={
        "id":task_id,
        "task":task_to_do,
        "status":status
    }
    tasks.append(task_data)
    print(f"{task_to_do} task added Successfully!..")
def view_task(tasks):
    for task in tasks:
        print(task)
def update_task(tasks,task_id):
    for task in tasks:
        if task['id']==task_id:
            while True:
                print("====UPDATE MENU====")
                print("1.update task id")
                print("2.update task to do")
                print("3.update task status")
                print("4.Exit")
                choice=int(input("Enter Your choice:"))
                if choice==1:
                    new_id=int(input("Enter new task id:-"))
                    for t in tasks:
                        if t["id"]==new_id:
                            print("this task_id is already exists!")
                            break
                    else:
                        task["id"] = new_id
                        print("Task id updated Successfully!.")
                elif choice==2:
                    new_task=input("Enter new task to do:-")
                    task['task']=new_task
                    print("Task Updated..")
                elif choice==3:
                    new_task_status=input("Enter new task status:-")
                    task['status']=new_task_status
                    print("Status Updated Successfully!")
                elif choice==4:
                    break
                else:
                    print("please choose valid option!")
            return
    print("No Task Found to this id!")
              
def mark_as_done(tasks,task_id):
    for task in tasks:
        if task['id']==task_id:
            task['status']="Successfully Task Completed!.."
            print(f"ID {task_id} task marked as Done!.")
            return
def delete_task(tasks,task_id):
    for i,task in enumerate(tasks):
        if task['id']==task_id:
            del tasks[i]
            print(f"Task deleted Successfully of id {task_id}")
            return

def menu():
    while True:
        print("===== To-Do List Application ===== ")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Mark Task as Done")
        print("5. Delete Task ")
        print("6. Exit ")
        choice=int(input("Enter Your Choice:-"))
        if choice==1:
            if len(tasks)>8:
                print("Oops! Tasks limit reached!..")
                continue
            try:
                task_id=int(input("Enter task id:-"))
                task_to_do=input("Enter task to do:")
                status=input("Enter task status:-")
                add_task(tasks,task_id,task_to_do,status)
            except ValueError:
                print("Invalid input.")
        elif choice==2:
            view_task(tasks)
        elif choice==3:
            task_id=int(input("Enter Task Id:-"))
            update_task(tasks,task_id)
        elif choice==4:
            task_id=int(input("Enter Task Id:-"))
            mark_as_done(tasks,task_id)
        elif choice==5:
            task_id=int(input("Enter Task Id:-"))
            delete_task(tasks,task_id)
        elif choice==6:
            break
        else:
            print("Choose valid Option!..")
if __name__=="__main__":
    menu()