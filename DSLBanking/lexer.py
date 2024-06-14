import re

class Token:
    def __init__(self, type, value, line, column):
        self.type = type
        self.value  = value
        self.line = line
        self.column = column

    def __repr__(self):
        return f'{self.type}({self.value})'

class Lexer:
    def __init__(self, code):
        self.code = code
        self.tokens = []
        self.tokenize()

    def tokenize(self):
        for token in self.tokenize_code():
            if token.type != 'SKIP' and token.type != 'NEWLINE':
                self.tokens.append(token)

    def tokenize_code(self):
        token_specification = [
            ('NUMBER',   r'\d+'), # integer
            ('ACCOUNT',  r'[A-Za-z]{2}\d{6}'), # alphanumeric account numbers 2 Alphabets followed by 6 numbers
            ('ID',       r'[A-Za-z]+'), # identifiers (words with only letters)
            ('SEMI',     r';'), # statement terminator
            ('SKIP',     r'[ \t]+|(?P<NEWLINE>\n)'), # spaces and tabs (excluding newline)
            ('MISMATCH', r'.'), # all other characters
        ]
        tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
        get_token = re.compile(tok_regex).match
        line_num = 1
        line_start = 0
        pos = 0
        mo = get_token(self.code)
        while mo is not None:
            typ = mo.lastgroup
            val = mo.group(typ)
            if typ == 'NEWLINE':
                line_start = pos
                line_num += 1
            elif typ != 'SKIP':
                column = mo.start() - line_start
                yield Token(typ, val, line_num, column)
            pos = mo.end()
            mo = get_token(self.code, pos) 
        if pos != len(self.code):
            raise RuntimeError('Unexpected character %r on line %d' % (self.code[pos], line_num))

# Usage
if __name__ == "__main__":
    code = """
    create account Marshall Korns with balance 999;
    deposit 999 to MK123456;
    withdraw 99 from MK123456;
    balance of MK123456;
    exit;
    """
    lexer = Lexer(code)
    for token in lexer.tokens:
        print(token)
