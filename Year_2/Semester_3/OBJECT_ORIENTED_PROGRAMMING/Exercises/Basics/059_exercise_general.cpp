/*
 * Exercise 14: Banking System with Transactions
 * 
 * Create a BankAccount base class with:
 * - Protected members: accountNumber (string), ownerName (string), balance (double)
 * - Constructor initializing all members
 * - Pure virtual methods: deposit(double amount), withdraw(double amount), calculateInterest()
 * - Virtual method getAccountInfo()
 * - Virtual destructor
 * 
 * Create two derived classes:
 * - SavingsAccount: additional member interestRate (double); 
 *   implement virtual methods with savings-specific behavior (interest calculated monthly)
 * - CheckingAccount: additional member transactionFee (double); 
 *   implement virtual methods with checking-specific behavior (fee applied to withdrawals)
 * 
 * Create a Bank class with:
 * - Private member: accounts (vector of BankAccount pointers)
 * - Method addAccount(BankAccount*) to add savings or checking accounts
 * - Method transfer(string fromAcc, string toAcc, double amount) between accounts
 * - Method displayAllAccounts() showing polymorphically
 * - Method findAccount(string accNum) returning account pointer or nullptr
 * - Destructor freeing all memory
 * 
 * In main(), create a bank with 3 savings and 2 checking accounts from user input, 
 * display all accounts, perform several transfers between accounts, 
 * calculate and apply interest to savings accounts, display updated balances, 
 * and ensure proper cleanup.
 */

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int main() {
    // Your code here
    
    return 0;
}
