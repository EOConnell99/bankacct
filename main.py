from bank_account import BankAccount
from savings import SavingsAccount
from checking import LimitedCheckingAccount

p1 = BankAccount("John", 20000, 2000, 1, 1)
p2 = BankAccount("Jeremy", 5000, 0, 2, 2)

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

a1 = SavingsAccount("Dexter", 35000, 1000, 3, 3, 0.05)
a2 = SavingsAccount("Doakes", 30000, 1000, 4, 4, 0.04)

a1.apply_interest()
print(a1.balance)
a1.deposit(1000)
a1.withdraw(3000)
print(a1.balance)

a2.apply_interest()
print(a2.balance)
a2.deposit(1500)
print(a2.balance)
a2.withdraw(5000000)
a2.withdraw(4000)
print(a2.balance)

b1 = LimitedCheckingAccount("Cody", 1000, 0, 5, 5, 100)
b2 = LimitedCheckingAccount("Aster", 1500, 0, 6, 6, 200)

b1.deposit(90)
print(b1.balance)
b1.deposit(10000)

b1.withdraw(50)
print(b1.balance)
b1.withdraw(1000)

b2.deposit(150)
print(b2.balance)
b2.deposit(1500)

b2.withdraw(100)
print(b2.balance)
b2.withdraw(15000)


