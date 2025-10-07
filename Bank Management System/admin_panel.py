
from data import customers,loan_requests
class Admin_menu:
    def reject_loan(self, loan_requests, customer_id):
        for loan_req in loan_requests:
            if loan_req['customer_id'] == customer_id:
                if loan_req['status'] != "Pending":
                    print("Loan has already been processed.")
                    return
                if loan_req['amount'] > 50000:
                    loan_req['status'] = "Loan Request Rejected"
                    loan_amt = loan_req['amount']
                    for customer in customers:
                        if customer_id == customer['id']:
                            customer['loan_requests'].append(f'₹{loan_amt}/- Loan Rejected')
                            print(f'₹{loan_amt}/- Loan Rejected')
                            return
                else:
                    print("Loan amount is within the limit and cannot be rejected.")
                    return
        print("Loan request not found for given customer ID.")

    def approve_loan(self,loan_requests,customer_id):
        flag=False
        for loan_req in loan_requests:
            if loan_req['customer_id']==customer_id:
                if loan_req['status'] != "Pending":
                    print("Loan has already been processed.")
                    return
                if loan_req['amount'] <= 50000:
                    loan_req['status']="Loan Approved"
                    loan_amt=loan_req['amount']
                    for customer in customers:
                        if customer_id==customer['id']:
                            customer['loan_requests'].append(f'₹{loan_amt}/- Loan Approved')
                            print(f"₹{loan_amt}/- Loan Approved")
                            a=customer['balance']
                            customer['balance']+=a
                            return
                else:
                    print("Loan amount exceeds ₹50,000. Cannot approve.")
                return
        else:
            print("Loan request not found for given customer ID.")



    def view_loan_requests(self,loan_requests,customers):
        for loan_req in loan_requests:
            print(loan_req)
    def view_all_accounts(self,customers):
        for customer in customers:
            print(customer)
    def run(self):
        while True:
            print("===== Admin Menu ===== ")
            print("1. View All Accounts ")
            print("2. View Loan Requests")
            print("3. Approve Loan")
            print("4. Reject Loan")
            print("5. Exit")
            choice=int(input("Enter your choice:-"))
            if choice==1:
                self.view_all_accounts(customers)
            elif choice==2:
                self.view_loan_requests(loan_requests,customers)
            elif choice==3:
                customer_id=int(input("Enter customer_id:-"))
                self.approve_loan(loan_requests,customer_id)
            elif choice==4:
                customer_id=int(input("Enter customer_id:-"))
                self.reject_loan(loan_requests,customer_id)
            elif choice==5:
                break
            else:
                print("Choose valid Option")

if __name__=="__main__":
    Admin_menu().run()
