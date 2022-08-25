filename = "p1.c" #input("Enter filename: ")
prog = open(filename)

whiteSpace = [" ", "\n", "\t", "\v", "\r", "\f"]
keywords = [ "auto", "break", "case", "char", "const", "continue", "default", "do", "double", "else", "enum", "extern", "float", "for", "goto", "if", "int", "long", "register", "return", "short", "signed", "sizeof", "static", "struct", "switch", "typedef", "union", "unsigned", "void", "volatile", "while",]
operators = ["+", "-", "*", "/", "%", "++", "--", "=", "+=", "-=", "*=", "/=", "%=", "==", "<", ">", "<=", ">=", "!=", "&&", "||", ]
separator = [",",";",":",".","(",")","[","]","{","}"]

def type(token):
    if token in keywords:
        return "keyword"
    elif token in operators:
        return "operator"
    elif token in separator:
        return "separator"
    else:
        return "identifier"

tokens_list = []

for line in prog:
    # preprocessing directory
    if line[0] == '#':
        continue
    
    word = ""
    oper = ""
    string_Flag = 0
    comment_Flag = 0
    for index in range(len(line)):
        i = line[index]

        # String literal:
        if string_Flag == 0:
            if i=='"':
                string_Flag = 1
        else:
            if i == '"' and word[-1] != "\\":
                tokens_list.append((word,type(word)))
                string_Flag = 0
                word = ""
            else:
                word = word + i
            continue

        # identifiers (strings and numbers) and keywords:
        if i.isalnum() or i == "_":
            word = word + i
        else:
            if len(word) != 0:
                tokens_list.append((word,type(word)))
                word = ""

        #check if operator:
        if i in operators:
            if len(oper) != 0:
                big_oper = oper + i
                print(big_oper)
                if big_oper in operators:
                    tokens_list.append((big_oper,type(big_oper)))
                else:
                    tokens_list.append((oper,type(oper)))
                    tokens_list.append((i,type(i)))
                oper = ""
            else:
                oper = i
        else:
            if len(oper) != 0:
                tokens_list.append((oper,type(oper)))
                oper = ""

        # seperators:
        if i in separator:
            tokens_list.append((i,type(i)))

no_operators = 0
no_separators = 0
no_identifiers = 0
no_keywords = 0

for token in tokens_list:
    print(token[1] + ": " + token[0])
    ttype = token[1]
    if ttype == "keyword":
        no_keywords += 1
    elif ttype == "separator":
        no_separators += 1
    elif ttype == "operator":
        no_operators += 1
    else:
        no_identifiers += 1

print("\n--- Details ---\n")
print("Identifiers  :", no_identifiers)
print("Keywords     :", no_keywords)
print("Separators   :", no_separators)
print("Operators    :", no_operators)