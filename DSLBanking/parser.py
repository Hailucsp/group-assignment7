from lexer import Lexer
###################################
##### AST NODE #####
###################################

# base class for AST nodes
class ASTNode:
    pass

# representation of the entire program as list of all the lines
class Program(ASTNode):
    def __init__(self):
        self.statements = []
    def __repr__(self):
        return f"Program(statements={self.statements})"

# representation of create account statement 
class CreateAccount(ASTNode):
    def __init__(self, first_name, last_name, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.balance = balance

    def __repr__(self):
        return f"CreateAccount(first_name={self.first_name}, last_name={self.last_name}, balance={self.balance})"

# representation of deposit statement 
class Deposit(ASTNode):
    def __init__(self, amount, account_number):
        self.amount = amount
        self.account_number = account_number

    def __repr__(self):
        return f"Deposit(amount={self.amount}, account_number={self.account_number})"


# representation of withdraw statement 
class Withdraw(ASTNode):
    def __init__(self, amount, account_number):
        self.amount = amount
        self.account_number = account_number

    def __repr__(self):
        return f"Withdraw(amount={self.amount}, account_number={self.account_number})"


# representation of check balance statement 
class Balance(ASTNode):
    def __init__(self, account_number):
        self.account_number = account_number

    def __repr__(self):
        return f"Balance(account_number={self.account_number})"

# representation of exit statement 
class Exit(ASTNode):
    pass

    def __repr__(self):
        return "Exit()"

###################################
##### PARSER #####
###################################

class Parser:
    # initialsing tokens, setting current token to None and index to -1 and then moving to the next (first) token
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = None
        self.pos = -1
        self.advance()

    # method to move the cursor - updates current token if in the range, and increments the position by 1
    def advance(self):
        self.pos += 1
        if self.pos < len(self.tokens):
            self.current_token = self.tokens[self.pos]
        else:
            self.current_token = None

    # parsing the list of tokens and returning program node depending on the current token value
    def parse(self):
        program = Program()
        while self.current_token is not None:
            if self.current_token.type == 'ID':
                if self.current_token.value == 'create':
                    program.statements.append(self.create_account())
                elif self.current_token.value == 'deposit':
                    program.statements.append(self.deposit())
                elif self.current_token.value == 'withdraw':
                    program.statements.append(self.withdraw())
                elif self.current_token.value == 'balance':
                    program.statements.append(self.balance())
                elif self.current_token.value in ('exit', 'quit', 'end'):
                    program.statements.append(Exit())
            self.advance()
        return program

    # parsing a create account statement : "create account Marshall Korns with balance 999;"
    def create_account(self):
        # print('Create account')
        self.advance()  # skipping 'create'
        self.advance()  # skipping 'account'
        first_name = self.current_token.value
        self.advance()
        last_name = self.current_token.value
        self.advance()
        self.advance()  # skipping 'with'
        self.advance()  # skipping 'balance'
        balance = self.current_token.value
        self.advance()  # skipping amount
        # self.advance()  # skipping ';' // not needed as we have one advance method called in the parser as well
        return CreateAccount(first_name, last_name, balance)

    # parsing a deposit statement : "deposit 999 to MK123456;"
    def deposit(self):
        # print('Deposit to account')
        self.advance()  # skipping 'deposit'
        amount = self.current_token.value
        self.advance()  # skipping amount
        self.advance()  # skipping 'to'
        account_number = self.current_token.value
        self.advance()  # skipping account_number
        # self.advance()  # skipping ';' // not needed as we have one advance method called in the parser as well
        return Deposit(amount, account_number)

    # parsing a withdraw statement : "withdraw 99 from MK123456;"
    def withdraw(self):
        self.advance()  # skipping 'withdraw'
        amount = self.current_token.value
        self.advance()  # skipping amount
        self.advance()  # skipping 'from'
        account_number = self.current_token.value
        self.advance()  # skipping account_number
        # self.advance()  # skipping ';' // not needed as we have one advance method called in the parser as well
        return Withdraw(amount, account_number)

    # parsing a balance statement : "balance of MK123456;"
    def balance(self):
        # print('Check balance')
        self.advance()  # skipping 'balance'
        self.advance()  # skipping 'of'
        account_number = self.current_token.value
        self.advance()  # skipping account_number
        # self.advance()  # skipping ';' // not needed as we have one advance method called in the parser as well
        return Balance(account_number)

# usage
if __name__ == "__main__":
    code = """
    create account Marshall Korns with balance 999;
    deposit 999 to MK123456;
    withdraw 99 from MK123456;
    balance of MK123456;
    exit;
    """
    lexer = Lexer(code)
    parser = Parser(lexer.tokens)
    ast = parser.parse()
    print(ast.statements)
