# Bank Accounts Management System

This repository contains a Python implementation of a simple Bank Account Management System, which includes the following classes:

1. BankAccount: Represents a basic bank account with methods for deposit, withdrawal, and balance inquiry.
2. InterestRewardsAcct: Inherits from BankAccount and adds functionality to provide a 5% interest reward on deposits.
3. SavingsAccount: Inherits from InterestRewardsAcct and introduces a fee on withdrawals.

### Table of Contents
* Installation
* Usage
* Classes
* Examples

### Installation

1. Clone the repository to your local machine: git clone https://github.com/RohanKumariya/Bank-Accounts-Management-System.git
2. Navigate to the project directory: cd bank-accounts
3. Run the main.py file: python main.py

### Usage

This Bank Account Management System provides a simple way to create and manage bank accounts, make deposits, withdrawals, and transfers. It includes three classes:

### Classes

*BankAccount*
* Represents a basic bank account with the following methods:
1. getBalance(): Prints the account's current balance.deposit(amount): Deposits the specified amount into the account.
2. withdraw(amount): Withdraws the specified amount from the account, withappropriate error handling for insufficient funds.
3. transfer(amount, account): Transfers the specified amount to another account,with error handling for insufficient funds.

*InterestRewardsAcct*
* Inherits from BankAccount and adds a 5% interest reward on deposits.

*SavingsAccount*
* Inherits from InterestRewardsAcct and introduces a withdrawal fee.
* Overrides the withdraw() method to account for the withdrawal fee.


### Examples
Here are some basic usage examples:

* Create a BankAccount
* Deposit money into the account
* Withdraw money from the account
* Create a SavingsAccount
* Deposit money into the savings account (with interest reward)
* Withdraw money from the savings account (with withdrawal fee)
* Transfer money between accounts



