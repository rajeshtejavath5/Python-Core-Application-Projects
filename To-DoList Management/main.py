from data import tasks
from todo_list import menu
def main():
    print("==== login to manage TO Do List ====")
    print("1.Login")
    print("2.Exit")
    choose=input("Enter your choice:-")
    if choose=='1':
        name=input("Enter name:-")
        pswd=input("Enter Password:-")
        if name=="rajesh" and pswd=="rajesh@321":
            print("Logged in Successfully!")
            menu()
        else:
            print("Invalid name/password")
if __name__=='__main__':
    main()
