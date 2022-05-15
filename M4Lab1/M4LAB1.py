# M4LAB1
# examples with Account class

from accountdoctest import Account
from decimal import Decimal

account1 = Account('John Green', Decimal('50.00'))

print(account1.name)
print(account1.balance)

account1.deposit(Decimal('25.53'))
print(account1.balance)
try:
    account1.deposit( Decimal('-123.45') )
except:
        print("I can't do that, Dave.")
        
# test withdraw
# account.withdraw(Decimal('-10.00'))
# account1.withdraw(Decimal('1000.00'))
account1.withdraw(Decimal('10.00'))
print(account1.balance)

# test name property
print(account1.name)
account1.name = "Bob Green"
print(account1.name)