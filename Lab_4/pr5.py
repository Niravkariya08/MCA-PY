class account:
    balance = 0
    
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

class deposit_amount:
    def deposit(self, amount):
        self.balance += amount
        print("\n===========================")
        print(f"Deposited {amount}.")

class withdraw_amount:
    def withdraw(self, amount):
        if amount > self.balance:
            print("\n===========================")
            print("Withdraw Fail Insufficient funds.")
        else:
            self.balance -= amount
            print("\n===========================")
            print(f"Withdrew {amount}.")
            
class userInfo(account, deposit_amount, withdraw_amount):

    def printData(self):
        print("\n===========================")
        print(f"Account Holder Name: {self.name}")
        print(f"Balance: {self.balance}\n")
        
class check_balance(userInfo):
    def checkBalance(self):
        print("\n===========================")
        print(f"Current Balance: {self.balance}\n\n")
        
userName = input("\nEnter your name: ")
userAmount = int(input("Enter your initial balance: "))
userData = check_balance(userName,userAmount)

class final_call:
    
    while True:
        print("\n===========================")
        print("1. Check Balance")
        print("2. Deposit Amount")
        print("3. Withdraw Amount")
        print("4. Exit")    
        
        choice = int(input("\nEnter your choice: "))
        if choice == 1:
            userData.checkBalance()
        elif choice == 2:
            deposit_amount = int(input("\nEnter the amount you want to deposit: "))
            userData.deposit(deposit_amount)
        elif choice == 3:
            withdraw_amount = int(input("\nEnter the amount you want to withdraw: "))
            userData.withdraw(withdraw_amount)
        elif choice == 4:
            print("\n===========================")
            print("Thank you for using our service.\n")
            break
        else:
            print("\n===========================")
            print("Invalid choice. Please try again.")