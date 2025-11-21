from bank_account import BankAccount
from savings import SavingsAccount
from checking import LimitedCheckingAccount

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


