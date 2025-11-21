from bank_account import BankAccount
class SavingsAccount(BankAccount):
    def __init__(self, name, balance, minimum_balance, account_number, routing_number, interest_rate):
        super().__init__(name, balance, minimum_balance, account_number, routing_number)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest_amount = self.balance * self.interest_rate
        self.balance += interest_amount