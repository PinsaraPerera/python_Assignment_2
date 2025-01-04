import json
import random


class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
        self.transaction_history = []
        self.loan_balance = 0

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited ${amount}")
        print(f"${amount} deposited successfully.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew ${amount}")
            print(f"${amount} withdrawn successfully.")
        else:
            print("Insufficient funds!")

    def view_balance(self):
        return self.balance

    def view_transaction_history(self):
        return self.transaction_history

    def apply_for_loan(self, principal, interest_rate, term_years):
        loan_amount = principal * (1 + interest_rate) ** term_years
        self.loan_balance += loan_amount
        self.transaction_history.append(f"Loan of ${loan_amount:.2f} approved.")
        print(f"Loan of ${loan_amount:.2f} approved successfully.")

    def view_loan_balance(self):
        return self.loan_balance


class BankingSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_holder):
        account_number = random.randint(100000, 999999)
        while account_number in self.accounts:
            account_number = random.randint(100000, 999999)
        new_account = BankAccount(account_number, account_holder)
        self.accounts[account_number] = new_account
        print(f"Account created successfully! Account Number: {account_number}")
        return account_number

    def find_account(self, account_number):
        return self.accounts.get(account_number)

    def save_to_file(self, filename):
        with open(filename, "w") as file:
            data = {
                account_number: {
                    "account_holder": account.account_holder,
                    "balance": account.balance,
                    "transaction_history": account.transaction_history,
                    "loan_balance": account.loan_balance,
                }
                for account_number, account in self.accounts.items()
            }
            json.dump(data, file, indent=4)
        print(f"Accounts saved to {filename}.")

    def load_from_file(self, filename):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                self.accounts = {
                    int(account_number): BankAccount(
                        account_number=int(account_number),
                        account_holder=details["account_holder"],
                        balance=details["balance"],
                    )
                    for account_number, details in data.items()
                }
                for account_number, details in data.items():
                    self.accounts[int(account_number)].transaction_history = details[
                        "transaction_history"
                    ]
                    self.accounts[int(account_number)].loan_balance = details[
                        "loan_balance"
                    ]
            print(f"Accounts loaded from {filename}.")
        except FileNotFoundError:
            print("File not found!")
        except json.JSONDecodeError:
            print("Error reading file. Please ensure it is correctly formatted.")


def menu():
    banking_system = BankingSystem()
    filename = "Banking_System/data.json"

    while True:
        print("\nAdvanced Banking System")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Apply for Loan")
        print("5. View Balance")
        print("6. View Transaction History")
        print("7. View Loan Balance")
        print("8. Save Accounts to File")
        print("9. Load Accounts from File")
        print("10. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            account_holder = input("Enter account holder name: ")
            banking_system.create_account(account_holder)
        elif choice == "2":
            try:
                account_number = int(input("Enter account number: "))
                account = banking_system.find_account(account_number)
                if account:
                    amount = float(input("Enter amount to deposit: "))
                    account.deposit(amount)
                else:
                    print("Account not found!")
            except ValueError:
                print("Invalid input!")
        elif choice == "3":
            try:
                account_number = int(input("Enter account number: "))
                account = banking_system.find_account(account_number)
                if account:
                    amount = float(input("Enter amount to withdraw: "))
                    account.withdraw(amount)
                else:
                    print("Account not found!")
            except ValueError:
                print("Invalid input!")
        elif choice == "4":
            try:
                account_number = int(input("Enter account number: "))
                account = banking_system.find_account(account_number)
                if account:
                    principal = float(input("Enter loan principal amount: "))
                    interest_rate = float(input("Enter annual interest rate (e.g., 0.05 for 5%): "))
                    term_years = int(input("Enter loan term in years: "))
                    account.apply_for_loan(principal, interest_rate, term_years)
                else:
                    print("Account not found!")
            except ValueError:
                print("Invalid input!")
        elif choice == "5":
            try:
                account_number = int(input("Enter account number: "))
                account = banking_system.find_account(account_number)
                if account:
                    print(f"Current Balance: ${account.view_balance():.2f}")
                else:
                    print("Account not found!")
            except ValueError:
                print("Invalid input!")
        elif choice == "6":
            try:
                account_number = int(input("Enter account number: "))
                account = banking_system.find_account(account_number)
                if account:
                    history = account.view_transaction_history()
                    if history:
                        print("Transaction History:")
                        for transaction in history:
                            print(transaction)
                    else:
                        print("No transactions found!")
                else:
                    print("Account not found!")
            except ValueError:
                print("Invalid input!")
        elif choice == "7":
            try:
                account_number = int(input("Enter account number: "))
                account = banking_system.find_account(account_number)
                if account:
                    print(f"Loan Balance: ${account.view_loan_balance():.2f}")
                else:
                    print("Account not found!")
            except ValueError:
                print("Invalid input!")
        elif choice == "8":
            banking_system.save_to_file(filename)
        elif choice == "9":
            banking_system.load_from_file(filename)
        elif choice == "10":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    menu()
