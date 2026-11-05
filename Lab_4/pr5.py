class account:
    balance = 0
    
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

class deposit_amount:
    def deposit(self, amount):
        self.balance += amount
        print(f"Transection is Done of Amount :{amount}")

class withdraw_amount:
    def withdraw(self, amount):
        if amount > self.balance:
            print("=============Withdraw Fail: Insufficient funds.=============")
        else:
            self.balance -= amount
            print(f"Transection is Done of Amount :{amount}.")
            
class userInfo(account, deposit_amount, withdraw_amount):
    def printData(self):
        print("===========================")
        print(f"Account Holder Name: {self.name}")
        print(f"Balance: {self.balance}\n")
        
class check_balance(userInfo):
    def checkBalance(self):
        print(f"\nCurrent Balance: {self.balance}")
        
userName = input("\nEnter your name: ")
userAmount = int(input("Enter your initial balance: "))
userData = check_balance(userName, userAmount)

# Print initial user info
userData.printData()

# Deposit an amount manually
print("Depositing 500...")
userData.deposit(500)

# Withdraw an amount manually
print("Withdrawing 200...")
userData.withdraw(200)
userData.checkBalance()