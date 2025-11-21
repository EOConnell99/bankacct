from bank_account import BankAccount

class LimitedCheckingAccount(BankAccount):
    def __init__(self, name, balance, minimum_balance, account_number, routing_number,  max_transfer):
        super().__init__(name, balance, minimum_balance, account_number, routing_number)
        self.max_transfer = max_transfer

    def deposit(self, amount):
        if amount > self.max_transfer:
            print("Deposit is too high")
        else:
            self.balance += amount

    def withdraw(self, amount):
        if amount > self.max_transfer:
            print("Withdraw amount exceeds the allowed limit.")
        elif self.balance - amount < self.minimum_balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount