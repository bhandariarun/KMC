class BankAccount:
    def __init__(self,account_number, balance, owner):
        self._account_number = account_number
        self._balance = balance
        self._owner = owner

    def get_account_number(self):
        return self._account_number

    def get_balance(self):
        return self._balance

    def get_owner(self):
        return self._owner

    def set_balance(self, balance):
        if balance >= 0:
            self._balance = balance
        else:
            print("The balance is a negative value")

    def set_owner(self, owner):
        if owner:
            self._owner = owner
        else:
            print("The owner name is empty")

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Successfully deposited {amount}. New balance: {self._balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0< amount <= self._balance:
            self._balance -= amount
            print(f"Withdraw {amount}. New balance: {self._balance}")
        else:
            print("Insufficient funds or invalid withdraw amounts.")

# Demonstration
if __name__ == "__main__":
    # Creating an instance of BankAccount
    account = BankAccount("123456789", 1000, "John Doe")

    # Accessing attributes using getters
    print("Account Number:", account.get_account_number())
    print("Balance:", account.get_balance())
    print("Owner:", account.get_owner())

    # Modifying attributes using setters
    account.set_balance(1500)
    account.set_owner("Jane Smith")

    # Depositing and Withdrawing funds
    account.deposit(500)
    account.withdraw(200)

    # Displaying updated information
    print("Updated Balance:", account.get_balance())