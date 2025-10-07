from data import customers,loan_requests
def view_loan_status(loan_requests, customers, name):
    for customer_det in customers:
        if customer_det.get('name')==name:
            cus_id=customer_det.get('id')
            break
    else:
        print("Entered Incorrect name!")
        return
    for cus_load_data in loan_requests:
        if cus_id==cus_load_data.get("customer_id"):
            print("Loan Status:")
            print(f"Amount: {cus_load_data['amount']}")
            print(f"Status: {cus_load_data['status']}")
            return
    print("There is no loan request on your name")
         
def apply_for_loan(loan_requests, customers, name, amount):
    if amount>50000:
        print("Requested Loan amount limit is out of Range!")
        return
    customer_loan_det={}
    for customer in customers:
        if customer['name']==name:
        # if customer.get('name')==name:
            customer_id=customer.get('id') #customer['id']
            break
    else:
        print("Entererd Incorrect name!")
        return
    for cus_loan_data in loan_requests:
        # loan_id=cus_loan_data.get("customer_id")
        # if customer_id==loan_id:
        if cus_loan_data['customer_id']==customer_id:
            previous_loan_amount=cus_loan_data.get('amount')
            if (previous_loan_amount+amount)>50000:
                print(f'''previous requested loan amount ₹{previous_loan_amount},\nCurrent Request loan amount ₹{amount}\nTotal Requested loan Amount is ₹{previous_loan_amount+amount}''')
                print("Requested Loan amount is greater than Actual loan limit! i.e ₹50,000/-")
                return
            else:
                    # loan_requests['customer_id']=id
                cus_loan_data['amount']+=amount
                print(f"Successfully you applied for loan ₹{amount}/- rupees")
                return
    new_loan_by_cus={
        "customer_id": customer_id,
        "amount": amount,
        "status": "Pending"
    }
    loan_requests.append(new_loan_by_cus)
    print(f"Loan request of ₹{amount} submitted successfully.")

        
def transfer_money(customers, name, pin,amount,receiver_name,id):
    if amount<=0:
        print("Tranfer Amount must be Greater than zero rupees!")
        return
    if name==receiver_name:
        print("Sender and Receiver cannot be Same Person/Account!")
        return

    flag=False
    for customer_det in customers:
        if customer_det.get("name")==name and customer_det.get("pin")==pin:
            BT=customer_det.get('balance')
            if amount>BT:
                print("Insufficient Balance to Transfer!")
                return
            customer_det['balance']-=amount
            AT=customer_det.get('balance')
            flag=True
            break
    else:
        print("Incorrect user Name/pin!")
    if flag:
        for customer_det in customers:
            if customer_det.get("name")==receiver_name and customer_det.get('id')==id:
                customer_det['balance']+=amount
                print(f"Successfully ₹{amount}/- transferred to {receiver_name}")
                return
        print("Incorrect Receiver Name/pin!")   

def withdraw_money(customers, name, pin, amount):
    if amount<=0:
        print("Withdraw Amount must be greater than ZERO rupees!")
        return
    for customer_det in customers:
        if customer_det.get("name")==name and customer_det.get("pin")==pin:
            if amount>customer_det.get('balance'):
                print("Insufficient balance!")
                return
            print(f" Account Holder Name: {customer_det.get('name')}")
            print(f" Your Previous balance is: ₹{customer_det.get('balance')}/-")
            customer_det['balance']-=amount
            print(f" ₹{amount}/- Withdrawn Successfully!\n Your current balance is ₹{customer_det.get('balance')}/-")
            return
    print("Incorrect pin/name!")

def deposit_money(customers, name, pin, amount):
    if amount<=0:
        print("Deposit Amount must be greater than ZERO rupees!")
        return
    for customer_det in customers:
        if customer_det.get("name")==name and customer_det.get("pin")==pin:
            print(f" Account Holder Name: {customer_det.get('name')}")
            print(f" Your Previous balance is: ₹{customer_det.get('balance')}/-")
            customer_det['balance']+=amount
            print(f" ₹{amount}/- Deposited Successfully!\n Your current balance is ₹{customer_det.get('balance')}/-")
            return customer_det['balance']
    print("Incorrect pin/name!")

def check_balance(customers, name, pin):
    for customer_det in customers:
        if customer_det.get("name")==name and customer_det.get("pin")==pin:
            print(f" Account Holder Name: {customer_det.get('name')}")
            print(f" Available Balance is: ₹{customer_det.get('balance')}/-")
            return
    print("Incorrect pin/name!")

def Customer_ui():
    while True:
        print("====== Customer Menu =====")
        print("1. Check Balance \n" \
        "2. Deposit Money \n" \
        "3. Withdraw Money \n" \
        "4. Transfer Money \n" \
        "5. Apply for Loan\n" \
        "6. View Loan Status \n" \
        "7. Exit ")
        choice=int(input("Enter your choice:-"))
        if choice==1:
            name=input("Enter your name:-")
            pin=int(input("Enter your pin:-"))
            check_balance(customers,name,pin)
        elif choice==2:
            name=input("Enter your name:-")
            pin=int(input("Enter your pin:-"))
            amount=int(input("Enter Deposit Amount:-"))
            deposit_money(customers,name,pin,amount)
        elif choice==3:
            name=input("Enter your name:-")
            pin=int(input("Enter your pin:-"))
            amount=int(input("Enter Withdraw Amount:-"))
            withdraw_money(customers,name,pin,amount)
        elif choice==4:
            name=input("Enter your name:-")
            pin=int(input("Enter your pin:-"))
            amount=int(input("Enter Amount to Transfer:-"))
            receiver_name=input("Enter Receiver Name:-")
            id=int(input("Enter Receiver Id:-"))
            transfer_money(customers, name, pin,amount,receiver_name,id)
        elif choice==5:
            name=input("Enter your name:-")
            amount=int(input("Enter Amount for Loan:-"))
            apply_for_loan(loan_requests, customers, name, amount) #loan_requests, customers, name, amount)     
        elif choice==6:
            name=input("Enter your name:-")
            view_loan_status(loan_requests, customers, name) 
        elif choice==7:
            break
        else:
            print("Choose correct Option")
if __name__=="__main__":
    Customer_ui()