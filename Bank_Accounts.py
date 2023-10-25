class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initial_Amount, acct_Name) -> None:
        self.balance = initial_Amount
        self.name = acct_Name

    def getBalance(self):
        print(f'\nAccount "{self.name}" has Balance = ${self.balance}')

    def deposit(self,amount):
        self.balance = self.balance + amount
        print(f'\nDeposit of {amount} completed')
        self.getBalance()

    def viableTransactions(self, amount):
        if self.balance > amount:
            return
        else:
            raise BalanceException(
                f"\nSorry account: '{self.name}' doesnt have enough funds for ${amount} transaction and has balance of {self.balance:.2f}"
            )
        
    def withdraw(self, amount):
        try:
            self.viableTransactions(amount)
            self.balance = self.balance - amount
            print(f'\nWithdraw of ${amount} complete.')
            self.getBalance()
        except BalanceException as error:
            print(f'\nWithdraw Incomplete: {error}')

    def transfer(self, amount, account):
        try:
            print('\n*****\n\nBeginning Transfer..')
            self.viableTransactions(amount)
            self.withdraw(amount) 
            account.deposit(amount)
            print('\nTransfer Complete\n\n*****')
        except BalanceException as error:
            print(f"\nTransfer Declined {self.name} doesn't have {amount} as balance\n\n*****")

class InterestRewardsAcct(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposit Complete")
        self.getBalance()

class SavingsAccount(InterestRewardsAcct):
    def __init__(self, initial_Amount, acct_Name) -> None:
        super().__init__(initial_Amount, acct_Name)
        self.fee = 5
    
    def withdraw(self, amount):
        try:
            self.viableTransactions(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print(f'\nWithdraw of {amount} complete.\nCurrent Balance = {self.balance}')
            self.getBalance()
        except BalanceException as error:
            print(f'\nWithdraw Incomplete: {error}')





        
        
