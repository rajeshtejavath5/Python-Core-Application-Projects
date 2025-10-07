class ATM:
    accounts= [
                                  {"name": "Ravi", "balance": 5000, "pin": 1234, "transactions": []}, 
                                  {"name": "Priya", "balance": 7000, "pin": 2345, "transactions": []}, 
                                  {"name": "Suresh", "balance": 10000, "pin": 3456, "transactions": []}, 
                                  {"name": "Anita", "balance": 3000, "pin": 4567, "transactions": []}, 
                                  {"name": "Kiran", "balance": 8500, "pin": 5678, "transactions": []},
                                  {"name": "Meena", "balance": 12000, "pin": 6789, "transactions": []}, 
                                  {"name": "Vamsi", "balance": 4500, "pin": 7890, "transactions": []},
                                  {"name": "Rohit", "balance": 6000, "pin": 8901, "transactions":[]},
                                  {"name": "Sonia", "balance": 9000, "pin": 9012, "transactions": []}, 
                                  {"name": "Neha", "balance": 11000, "pin": 1122, "transactions":[]}
                                  ]
    def check_balance(self,entered_name,entered_pin):
        for acc_holder_det in self.accounts:
            if acc_holder_det.get("name")==entered_name and acc_holder_det.get("pin")==entered_pin:
                print(f" Account Holder Name: {acc_holder_det.get('name')}")
                print(f" Your Balance is: ₹{acc_holder_det.get('balance')}")
                break
        else:
            print("Invalid name or pin, Please Enter correct Details")

    def deposit_money(self,entered_name,entered_pin):
        depo_amt=int(input("Enter deposit amount:-"))
        if depo_amt<=0:
            print("deposit amount must be in positive number: - i.e greater than 'zero'")
        else:
            for acc_holder_det in self.accounts:
                if acc_holder_det.get("name")==entered_name and acc_holder_det.get("pin")==entered_pin:
                    print(f"Your Previous balance is ₹{acc_holder_det.get('balance')}")
                    acc_holder_det['balance']+=depo_amt
                    acc_holder_det['transactions'].append(f"Deposited ₹{depo_amt} Successfully")
                    print(f"₹{depo_amt} Deposited Successfully!\n Your current balance is ₹{acc_holder_det.get('balance')}")
                    break
            else:
                print("Invalid name or pin, Please Enter correct Details")   
    def withdraw_money(self,entered_name,entered_pin):
        withdraw_amt=int(input("Enter Withdraw amount:-"))
        if withdraw_amt<=0:
            print("withdraw amount must be in positive number: - i.e greater than 'zero'")
        else:
            for acc_holder_det in self.accounts:
                if acc_holder_det.get("name")==entered_name and acc_holder_det.get("pin")==entered_pin:
                    if acc_holder_det.get("balance")<=0 or withdraw_amt>acc_holder_det.get("balance"):
                        print("Insufficient balance!")
                        return
                    else:
                        print(f"Your Previous balance is ₹{acc_holder_det.get('balance')}")
                        acc_holder_det['balance']-=withdraw_amt
                        acc_holder_det['transactions'].append(f"Withdraw ₹{withdraw_amt} Successfully")
                        print(f"₹{withdraw_amt} Withdraw Successfully!\n Your current balance is ₹{acc_holder_det.get('balance')}")
                        break
                else:
                    print("Invalid name or pin, Please Enter correct Details")
                    break
        
    def transaction_history(self,entered_name,entered_pin):
        for acc_holder_det in self.accounts:
            if acc_holder_det.get('name')==entered_name and acc_holder_det.get('pin')==entered_pin:
                th=acc_holder_det.get('transactions')
                print(th)
                break
        else:
            print("Invalid name or pin, Please Enter correct Details!")

    def run(self):
        while True:
            print("====== ATM MACHINE ======")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Transaction History")
            print("5. Exit")
            choice = int(input("Enter your choice:-"))
            if choice==1:
                entered_name=input("Enter Your Name:-")
                entered_pin=int(input("Enter Your PIN:-"))
                self.check_balance(entered_name,entered_pin)
            elif choice==2:
                name=input("Enter Your Name:-")
                pin=int(input("Enter your PIN:-"))
                self.deposit_money(name,pin)
            elif choice==3:
                name=input("Enter Your Name:-")
                pin=int(input("Enter your PIN:-"))
                self.withdraw_money(name,pin)
            elif choice==4:
                name=input("Enter Your Name:-")
                pin=int(input("Enter your PIN:-"))
                self.transaction_history(name,pin)
            elif choice==5:
                break
            else:
                print("please choose valid option")
if __name__=="__main__": 
    ATM().run()