# to run actual tests
import unittest
# to check terminal outputs
import io
import sys
# base created for the exercise
from lexer import Lexer
from parser import Parser, CreateAccount, Deposit, Withdraw, Balance, Exit
from banking import Banking

class TestDSL(unittest.TestCase):
    def run_code(self, code):
        #using lexer, parser and Banking class to check the output
        lexer = Lexer(code)
        parser = Parser(lexer.tokens)
        ast = parser.parse()
        banking = Banking()        
        captured_output = io.StringIO()
        sys.stdout = captured_output
        try:
            banking.execute(ast.statements)
        except Exception as e: #added exception handler for cases that raise error - eg, the withdraw over balance test.
            print(e)
        sys.stdout = sys.__stdout__
        return captured_output.getvalue().strip().split('\n') #getting terminal output and converting to list of lines

    #code below just passes the code to run banking code, gets the output, and compares it with the expected output. 
    def test_create_account(self):
        code = """
        create account Marshall Korns with balance 999;
        balance of MK000001;
        """
        expected_output = [
            "Account MK000001 created for Marshall Korns with balance 999",
            "Balance for MK000001 is 999"
        ]
        actual_output = self.run_code(code)
        self.assertEqual(actual_output, expected_output)

    def test_deposit(self):
        code = """
        create account Alice B with balance 500;
        deposit 200 to AB000001;
        balance of AB000001;
        """
        expected_output = [
            "Account AB000001 created for Alice B with balance 500",
            "Deposited 200 to AB000001. New balance is 700",
            "Balance for AB000001 is 700"
        ]
        actual_output = self.run_code(code)
        self.assertEqual(actual_output, expected_output)

    def test_withdraw(self):
        code = """
        create account Bob Smith with balance 300;
        withdraw 100 from BS000001;
        balance of BS000001;
        """
        expected_output = [
            "Account BS000001 created for Bob Smith with balance 300",
            "Withdrew 100 from BS000001. New balance is 200",
            "Balance for BS000001 is 200"
        ]
        actual_output = self.run_code(code)
        self.assertEqual(actual_output, expected_output)

    def test_insufficient_funds(self):
        code = """
        create account John Appleseed with balance 100;
        withdraw 200 from JA000001;
        """
        expected_output = [
            "Account JA000001 created for John Appleseed with balance 100",
            "Insufficient funds in account JA000001."
        ]
        actual_output = self.run_code(code)
        self.assertEqual(actual_output, expected_output)

def specification_tests(): #method name specified in the assignment
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDSL) #loading and running the tests
    unittest.TextTestRunner().run(suite)

specification_tests()
