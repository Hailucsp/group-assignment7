class BankAccount:
    def __init__(self, fName, lName, accountDigits ,balance = 0):
      self.balance = balance
      self.accountID = self.accountID()
      self.fName = fName
      self.lName = lName
      self.accountDigits = accountDigits

    def accountValidator(self):
        if len(self.accountDigits) != 6:
            return False
        if not self.accountDigits.isdigit():
            return False
    def accountID(self):
        if self.accountValidator() == True:
            return f"{self.fName[0]}{self.lName[0]}{self.accountDigits}"
    def deposit(self):
        amount = float(input("Enter an amount: "))
        self.balance += amount
        print("Amount Deposited: ", amount)
        print("Balance: ", self.balance)

    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance>=amount:
            self.balance-=amount
            print("\n You Withdrew:", amount)
            print("Balance: ", self.balance)
        else:
            print("\n Insufficient balance  ")

      
# getters and setters
def getfName(self):
   return self.fName
def setfName(self, fn):
   self.fName = fn

def getlName(self):
   return self.lName
def setlName(self, ln):
   self.lName = ln

def getAccountDigits(self):
   return self.accountDigits
def setAccountDigits(self, aD):
   self.accountDigits = aD

def getBalance(self):
   return self.balance
def setBalance(self, newBal): 
    self.balance = newBal 

def getAccountID(self):
        return self.accountID
