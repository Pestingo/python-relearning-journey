class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: ${amount:.2f}. New balance: ${self.balance:.2f}")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")
    
    def check_balance(self):
        print(f"Account holder: {self.account_holder}")
        print(f"Current balance: ${self.balance:.2f}")
    
    def __str__(self):
        return f"{self.account_holder} - Balance: ${self.balance:.2f}"


# Main program
if __name__ == "__main__":
    account = BankAccount("Pester Mbhetse", 1000)
    
    print("=== Bank Account Application ===\n")
    account.check_balance()
    
    print("\n--- Transactions ---")
    account.deposit(500)
    account.withdraw(200)
    account.withdraw(2000)
    account.deposit(-100)
    
    print("\n--- Final Balance ---")
    account.check_balance()
