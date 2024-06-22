def lexer(contents):
    lines = contents.split('\n')

    nLines = []
    for line in lines:
        chars = list(line)
        tokens = []
        temp_str = ""
        quote_count = 0
        for char in chars:
            if char == '"' or char == "'":
                quote_count += 1
            if quote_count % 2 ==0:
                in_quotes = False
            else:
                in_quotes = True

            if cha4r == " " and in_quotes == False:
                tokens.append(temp_str)
                temp_str = ""
            else:
                temp_str += char
        tokens.append(temp_str)
        items = []
        for token in tokens:
            if token[0] == "'" or token[0] == '"':
                if token[-1] == '"' or toekn[-1] == "'":
                    itmes.append(("string", token))
                else:
                    break
            elif re.match(r"[.a-zA-Z]+", token):
                items.append(("symbol", token))
            elif token in "+-*/=":
                items.append(("expression", token))
            elif re.match(r"[.0-9]+", token):
                items.append(("number", token))
        nLines.append(items)
    return nLine
    
def parse(file): 
  contents = open(file, "r").read()
  token = lexer(contents)
  return tokens
