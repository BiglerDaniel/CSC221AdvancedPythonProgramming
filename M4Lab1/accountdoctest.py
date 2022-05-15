# accountdoctest.py
"""Account class definition."""
from decimal import Decimal

class Account:
    """Account class for demonstrating doctest."""
    
    def __init__(self, name, balance):
        """Initialize an Account object.
        
        >>> account1 = Account('John Green', Decimal('50.00'))
        >>> account1.name
        'John Green'
        >>> account1.balance
        Decimal('50.00')

        The balance argument must be greater than or equal to 0.
        >>> account2 = Account('John Green', Decimal('-50.00'))
        Traceback (most recent call last):
            ...
        ValueError: Initial balance must be >= to 0.00.
        """

        # if balance is less than 0.00, raise an exception
        if balance < Decimal('0.00'):
            raise ValueError('Initial balance must be >= to 0.00.')

        self.name = name
        self.balance = balance

    def deposit(self, amount):
        """Deposit money to the account.
        >>> from accountdoctest import Account
        >>> from decimal import Decimal
        >>> account = Account("John Doe", Decimal("50.00"))
        >>> account
        Account(name='John Doe',balance=50.00)
        >>> str(account)
        'Account balance for John Doe is $50.00'
        >>> account.deposit(Decimal('10.00'))
        >>> account.balance
        Decimal('60.00')"""

        # if amount is less than 0.00, raise an exception
        if amount < Decimal('0.00'):
            raise ValueError('amount must be positive.')

        self.balance += amount
        
    def withdraw(self, amount):
        """ withdraw money form the account 
        >>> account = Account("John Doe", Decimal("50.00"))
        >>> account
        Account(name='John Doe',balance=50.00)
        >>> str(account)
        'Account balance for John Doe is $50.00'
        >>> account.withdraw(Decimal('10.00'))
        >>> account.balance
        Decimal('40.00')
        """
        #if amount > balance, raise exception
        if amount > self.balance:
            raise ValueError('account must be <= to balance')
        elif amount< Decimal('0.00'):
            raise ValueError('amount must be positive')
            
        self.balance -= amount
        
    @property
    def name(self):
        """ return the accountname """
        return self._name
    
    @name.setter
    def name(self, name):
        if len(name) <= 0:
            raise ValueError ("Account name cannot be empty")
            
        self._name = name
        
    def __str__(self):
        return ( "Account balance for " + self._name + " is $" + str(self.balance) )
    
    def __repr__(self):
        return ( "Account(name='" + self.name + "',balance=" + str(self.balance)+")" )

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
