from lexer import Lexer
from parser import Parser, CreateAccount, Deposit, Withdraw, Balance, Exit

class Banking:
    def __init__(self):
        self.accounts = {} #object to hold the accounts 
        self.account_counter = 1  # counter for generating unique account numbers

    def check_accounts_existence(self, account_number):
        #since this is used multiple times, made a function to check if account number already exists
        if account_number in self.accounts:
            return True

    def create_account(self, first_name, last_name, balance):
        #function that takes in first name, last name and balance to create an account. the counter is used to generate the account number digit.
        account_number = (first_name[0] + last_name[0]).upper() + f"{self.account_counter:06d}"
        if self.check_accounts_existence(account_number):
            raise ValueError(f"Account {account_number} already exists.")
        self.accounts[account_number] = {
            "first_name": first_name,
            "last_name": last_name,
            "balance": int(balance)
        }
        print(f"Account {account_number} created for {first_name} {last_name} with balance {balance}") #printing the result
        return account_number

    def deposit(self, amount, account_number):
        if not self.check_accounts_existence(account_number):
            raise ValueError(f"Account {account_number} does not exist.")
        self.accounts[account_number]["balance"] += int(amount) #adding amount to a particular account
        print(f"Deposited {amount} to {account_number}. New balance is {self.accounts[account_number]['balance']}")
        return {"account_number":account_number,"balance":self.accounts[account_number]['balance']}

    def withdraw(self, amount, account_number):
        if not self.check_accounts_existence(account_number):
            raise ValueError(f"Account {account_number} does not exist.")
        if self.accounts[account_number]["balance"] < int(amount):
            raise ValueError(f"Insufficient funds in account {account_number}.") #handling case where there is no sufficient balance
        self.accounts[account_number]["balance"] -= int(amount) # reducing the entered amount from account's balance
        print(f"Withdrew {amount} from {account_number}. New balance is {self.accounts[account_number]['balance']}") #printing the result
        return {"account_number":account_number,"balance":self.accounts[account_number]['balance']}

    def balance(self, account_number):
        if not self.check_accounts_existence(account_number):
            raise ValueError(f"Account {account_number} does not exist.")
        print(f"Balance for {account_number} is {self.accounts[account_number]['balance']}") #printing the balance
        return {"account_number":account_number,"balance":self.accounts[account_number]['balance']}

    def execute(self, statements):
        for statement in statements:
            if isinstance(statement, CreateAccount):
                self.create_account(statement.first_name, statement.last_name, statement.balance)
            elif isinstance(statement, Deposit):
                self.deposit(statement.amount, statement.account_number)
            elif isinstance(statement, Withdraw):
                self.withdraw(statement.amount, statement.account_number)
            elif isinstance(statement, Balance):
                self.balance(statement.account_number)
            elif isinstance(statement, Exit):
                print("Closing the Banking program.")
                break

# usage
# MK000001 will be the first account number for Marshall Korns
if __name__ == "__main__":
    code = """
    create account Marshall Korns with balance 999;
    deposit 999 to MK000001;
    withdraw 99 from MK000001;
    balance of MK000001;
    exit;
    """
    lexer = Lexer(code)
    parser = Parser(lexer.tokens)
    ast = parser.parse()
    banking = Banking()
    banking.execute(ast.statements)
