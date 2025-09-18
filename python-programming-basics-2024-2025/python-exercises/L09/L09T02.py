# The Account class manages the account balance and its modifications
class Account:
    # Initializes the account with the given initial balance
    def __init__(self, initial_balance: float = 0):
        if initial_balance < 0:
             raise ValueError("Initial balance cannot be negative.")
        self._balance = initial_balance

    # Property balance returns the current balance of the account
    @property
    def balance(self):
        return self._balance

    # The add method adds the given amount to the account
    def add(self, amount: float) -> float:
        if amount < 0:
            raise ValueError("Amount to add cannot be negative.")
        self._balance += amount
        return self._balance
    
     # The withdraw method attempts to withdraw the given amount from the account
    def withdraw(self, amount: float) -> float:
        if amount < 0:
            raise ValueError("Amount to withdraw cannot be negative.")
        if amount > self._balance:
            raise ValueError(f"Sorry, you have only {self._balance}€, the withdrawal cannot be completed.")
        self._balance -= amount
        return self._balance

# Helper function to create a new Account object with the given initial balance
def create_account(initial_balance: float = 0) -> Account:
    try:
        return Account(initial_balance)
    except ValueError as e:
        print(f"Error creating account: {e}")

# Helper function that asks the user for an amount to add to the account
def handle_add(account: Account) -> None:
    try:
        amount = float(input("How many euros will be added? "))
        account.add(amount)
    except ValueError as e:
        print(f"Error: {e}")

# Helper function that asks the user for an amount to withdraw from the account
def handle_withdraw(account: Account) -> None:
    try:
        amount = float(input("How many euros will be withdrawn? "))
        account.withdraw(amount)
    except ValueError as e:
        print(f"Error: {e}")

# Define main
def main():
    account = create_account(2000)
    print("Bank account created.")
    print(f"Bank account balance: {account.balance}€")
    handle_add(account)
    print(f"Bank account balance: {account.balance}€")
    handle_withdraw(account)
    print(f"Bank account balance: {account.balance}€")
    handle_withdraw(account)

# Start main
if __name__ == "__main__":
    main()