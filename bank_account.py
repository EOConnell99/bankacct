class BankAccount:
    bank_title = "Chase" #Should be the same across all accounts methinks
    def __init__(self, name, balance, minimum_balance, account_number, routing_number):
        self.name = name
        self.balance = balance
        self.minimum_balance = minimum_balance
        self._account_number = account_number
        self.__routing_number = routing_number
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if self.balance - amount > self.minimum_balance:
            self.balance -= amount
        else:
            print("Insufficient balance")
    def print_customer_information(self):
        print("Bank Name: " + self.bank_title + ", Customer Name: " + self.name + ", Balance: " + str(self.balance) + ", Minimum Balance: " + str(self.minimum_balance))
