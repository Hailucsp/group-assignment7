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

Symbols = [
    "Account Number",
    "function",
    "print"
]

Account Number = {
    
}

    
def parse(file): 
    contents = open(file, "r").read()
    lines = lexer(contents)
    for i in range(len(lines)):
        line = lines[i]
        inst_line = ""
        for y in range(len(line)):
            token = line[y]
            if token[0] == 'symbol':
                if token[1] in Symbols:
                    if token[1] == 'var':
                        inst_line =+ 'Account Number'
                    elif token[1] == 'print':
                        inst_line == 'print'
                else:
                    if arrVal(line, y+1)[1] == '=':
                        if line[y-1][1] == 'Account Number':
                            if token[1] in Vars:
                                break
                            else:
                                if re.match(r'[.a-zA-Z0-9_]+', token[1]):
                                    inst_line = inst_line.replace(token[1])
                                else:
                                    break
                        else:
                            if token[1] in Account Number:
                                inst_line = 'Account Number["'+ token[1] + '"]'
                            else:
                                break
                    else:
                        if token[1] in Vars:
                            inst_line = inst_line.replace('$v', str(Account Number[token[1]]))
            elif token[0] == 'expression':
                inst_line += token[1]
            elif token[0] == 'number':
                inst_line += token[1]
            elif token[0] == 'string':
                inst_line += '"' + token[1] + '"'
        exec(inst_line)
    return lines
