from Bank_Accounts import *

Rohan = BankAccount(1000, "Rohan")
Tanay = BankAccount(2000, "Tanay")
Tarun = BankAccount(4000, "Tarun")
Nary = BankAccount(2000, "Nary")
Rohan.getBalance()

Tanay.getBalance()

Rohan.deposit(1000)

Rohan.transfer(2000, Tanay)

Rashmi = InterestRewardsAcct(1000, 'Rashmi')

Rashmi.getBalance()

Rashmi.deposit(100)

Rashmi.transfer(5, Rohan)

Ritu = SavingsAccount(1000, 'Ritu')

Ritu.getBalance()

Ritu.transfer(200, Tanay)

Ritu.getBalance()
