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


