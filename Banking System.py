class Banksys:
    def __init__(self):
        self.accounts = {}
        self.transaction_history = {}

    def record_trans(self, accountno, trans_type, amount):
        if accountno in self.transaction_history:
            self.transaction_history[accountno].append({'type': trans_type, 'amount': amount})
        else:
            self.transaction_history[accountno] = [{'type': trans_type, 'amount': amount}]

    def create_account(self, accountno, name, initial_bal):
        if accountno in self.accounts:
            print("Account already exists")
        else:
            self.accounts[accountno] = {'Name': name, 'Balance': initial_bal}
            self.record_trans(accountno, 'Initial Deposit', initial_bal)
            print("Account Created Successfully")

    def login(self, accountno):
        if accountno in self.accounts:
            print("Welcome, {}".format(self.accounts[accountno]['Name']))
            return accountno
        else:
            print("Account not found")
            return None

    def check_balance(self, accountno):
        if accountno in self.accounts:
            print("Current Balance: {:.2f}".format(self.accounts[accountno]['Balance']))
        else:
            print("Account not found")

    def deposit(self, accountno, amount):
        if accountno in self.accounts:
            if amount > 0:
                self.accounts[accountno]['Balance'] += amount
                self.record_trans(accountno, 'Deposit', amount)
                print("Deposited {:.2f} successfully.".format(amount))
                self.check_balance(accountno)  # Display updated balance
            else:
                print("Invalid amount. Please enter a positive value.")
        else:
            print("Account not found")

    def withdraw(self, accountno, amount):
        if accountno in self.accounts:
            if amount > 0:
                if self.accounts[accountno]['Balance'] >= amount:
                    self.accounts[accountno]['Balance'] -= amount
                    self.record_trans(accountno, 'Withdrawal', amount)
                    print("Withdrawn {:.2f} successfully".format(amount))
                    self.check_balance(accountno)  # Display updated balance
                else:
                    print("Insufficient Balance")
            else:
                print("Invalid amount. Please enter a positive value.")
        else:
            print("Account not found")

    def close_account(self, accountno):
        if accountno in self.accounts:
            del self.accounts[accountno]
            if accountno in self.transaction_history:
                del self.transaction_history[accountno]
            print("Account closed successfully.")
        else:
            print("Account not found.")

    def display_account_details(self, accountno):
        if accountno in self.accounts:
            account_info = self.accounts[accountno]
            print("Account Number: {}".format(accountno))
            print("Account Holder: {}".format(account_info['Name']))
            print("Current Balance: {:.2f}".format(account_info['Balance']))
        else:
            print("Account not found")

    def display_welcome_message(self):
        print("Welcome to Our Banking System!")
        print("Please select an option from the menu below:")

    def display_menu(self):
        print("\n==== Banking System Menu ====")
        print("1. Create Account")
        print("2. Login")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Check Balance")
        print("6. View Transaction History")
        print("7. Display Account Details")
        print("8. Close Account")
        print("9. Exit")


# Main Program
bank = Banksys()
current_account = None

while True:
    bank.display_welcome_message()
    bank.display_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        account_number = input("Enter Account Number: ")
        name = input("Enter Name: ")
        initial_balance = float(input("Enter Initial Balance: "))
        bank.create_account(account_number, name, initial_balance)

    elif choice == '2':
        account_number = input("Enter Account Number: ")
        current_account = bank.login(account_number)  # Set current_account upon successful login

    elif choice == '3':
        if current_account:
            amount = float(input("Enter Amount to Deposit: "))
            bank.deposit(current_account, amount)
        else:
            print("Please login first.")

    elif choice == '4':
        if current_account:
            amount = float(input("Enter Amount to Withdraw: "))
            bank.withdraw(current_account, amount)
        else:
            print("Please login first.")

    elif choice == '5':
        if current_account:
            bank.check_balance(current_account)
        else:
            print("Please login first.")

    elif choice == '6':
        if current_account:
            if current_account in bank.transaction_history:
                print("Transaction History for Account {}".format(current_account))
                for transaction in bank.transaction_history[current_account]:
                    print("Type: {}, Amount: {:.2f}".format(transaction['type'], transaction['amount']))
            else:
                print("No transaction history available.")
        else:
            print("Please login first.")

    elif choice == '7':
        if current_account:
            bank.display_account_details(current_account)
        else:
            print("Please login first.")


    elif choice == '8':

        if current_account:
            bank.close_account(current_account)
            current_account = None
        else:
            print("Please login first.")


    elif choice == '9':
        print("Thank you for using our Banking System!")
        break

    else:
        print("Invalid choice. Please try again.")
