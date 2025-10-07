from customer_panel import Customer_ui
from admin_panel import Admin_menu
from data import Admin_data
def main():
    print("==== Welcome to the Rajesh Bank System ====")
    while True:
        print("Login as:")
        print("1. Customer")
        print("2. Admin")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice=="1":
            Customer_ui()
        elif choice=="2":
            user_name=input("Enter name:")
            password=input("Enter Password:")
            for admin in Admin_data:
                if user_name== admin['name']and password==admin['password']:
                    Admin_menu().run()
            else:
                print("Incorrect Password!")
        elif choice=="3":
            print("Thank You!")
            break
        else:
            print("Invalid option choosed. Try again!")

if __name__=="__main__":
    main()