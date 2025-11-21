class BankAccount:
    bank_title = "Chase" #Should be the same across all accounts methinks
    def __init__(self, name, balance, minimum_balance):
        self.name = name
        self.balance = balance
        self.minimum_balance = minimum_balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if self.balance - amount > self.minimum_balance:
            self.balance -= amount
        else:
            print("Insufficient balance")
    def print_customer_information(self):
        print("Bank Name: " + self.bank_title + ", Customer Name: " + self.name + ", Balance: " + str(self.balance) + ", Minimum Balance: " + str(self.minimum_balance))


class SavingsAccount(BankAccount):
    def __init__(self, name, balance, minimum_balance, interest_rate):
        super().__init__(name, balance, minimum_balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest_amount = self.balance * self.interest_rate
        self.balance += interest_amount
class LimitedCheckingAccount(BankAccount):
    def __init__(self, name, balance, minimum_balance, max_transfer):
        super().__init__(name, balance, minimum_balance)
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

p1 = BankAccount("John", 20000, 2000)
p2 = BankAccount("Jeremy", 5000, 0)

p1.deposit(100)
print(p1.balance)
p1.withdraw(200)
print(p1.balance)

p2.deposit(500)
print(p2.balance)
p2.withdraw(6000)
print(p2.balance)

p1.print_customer_information()
p2.print_customer_information()


