employees=[
    {"id": 1, "name": "Alice", "department": "HR", "role": "Manager", "salary": 50000}, 
{"id": 2, "name": "Bob", "department": "IT", "role": "Developer", "salary": 60000}]
def delete_emp(ename,eid):
    for i,emp in enumerate(employees):
        if emp['name']==ename and emp['id']==eid:
            del employees[i]
            print(f"Employee {ename} with id {eid} Deleted Successfully!..")
            return
    print("Invalid employee name/id\nOr user not exist!..")

    pass
def update_emp(ename, eid):#update employee details by receiving two inputs as parameters
    for emp in employees:
        if emp["name"] == ename and emp["id"] == eid:
            while True:
                print("===== Update Employee Details =====")
                print("1. Update Name")
                print("2. Update Department")
                print("3. Update Role")
                print("4. Update Salary")
                print("5. Exit")
                choose = int(input("Choose one option to perform operation: "))

                if choose == 1:
                    new_name = input("Enter new name: ")
                    emp["name"] = new_name
                    print("Name updated successfully.")
                elif choose == 2:
                    new_dept = input("Enter new department: ")
                    emp["department"] = new_dept
                    print("Department updated successfully.")
                elif choose == 3:
                    new_role = input("Enter new role: ")
                    emp["role"] = new_role
                    print("Role updated successfully.")
                elif choose == 4:
                    new_salary = float(input("Enter new salary: "))
                    emp["salary"] = new_salary
                    print("Salary updated successfully.")
                elif choose == 5:
                    print("Exiting update menu.")
                    break
                else:
                    print("choose correct Option")
            return
    print("Entered invalid name/id")

                   
    
def search_emp(emp_name,emp_id):
    for emp in employees:
        if emp['name']==emp_name and emp['id']==emp_id:
            print(emp)
            return
def view_emp():
    for emp in employees:
        print(emp)
def add_emp(e_id,e_name,e_dept,e_role,e_sal):
    employee_det={}
    employee_det["id"]=e_id
    employee_det["name"]=e_name
    employee_det['department']=e_dept
    employee_det['role']=e_role
    employee_det['salary']=e_sal
    for emp in employees:
        if emp['id']==e_id and emp['name']==e_name:
            print("User already exists!..")
            return
    employees.append(employee_det)
    print(f"{e_name} employee details are Successfully Updated!")
    
def menu():#this all about menu bar, from we can choose our required function
    while True:
        print("===== Employee Management System ===== ")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee ")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Exit ")
        choice=int(input("Enter Your Choice:"))
        if choice==1:
            if len(employees)>8:
                print("maximum Employees are already added ,limit reached to 8 emp")
                break
            else:
                emp_id=int(input("Enter Employee Id:-"))
                name=input("Enter Employee Name:-")
                emp_dept=input("Enter Employee Department:-")
                emp_role=input("Enter Employee Job Role:-")
                emp_sal=float(input("Enter employee salary:-"))
                add_emp(emp_id,name,emp_dept,emp_role,emp_sal)
        elif choice==2:
            view_emp()
        elif choice==3:
            emp_name=input("Please Enter your name:-")
            emp_id=int(input("Enter Empoyee id:-"))
            search_emp(emp_name,emp_id)
        elif choice==4:
            emp_name=input("Please Enter your name:-")
            emp_id=int(input("Enter Empoyee id:-"))
            update_emp(emp_name,emp_id)
        elif choice==5:
            emp_name=input("Please Enter your name:-")
            emp_id=int(input("Enter Empoyee id:-"))
            delete_emp(emp_name,emp_id)
        elif choice==6:
            break
        else:
            print("Chosse valid Option")
menu()