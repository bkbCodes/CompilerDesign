# Non deterministic grammar to deterministic grammar converions

# Global variables:
filename = "NDG_to_DG/Grammar"    # file to be read
file = open(filename)   # open the specified file and read the Grammar
productions = {}        # store produtions rules {symbols: rules} eg. A->a/b is stored as {"A":["a","b"]}
symbols = []            # variable ie non terminal symbols
terminals = []          # terminals
startSymbol = ""

# spilting the rules into terminal and non terminal symbols
def parseSymbols(symbolsTable, productions):
    for s in symbolsTable:
        for rid in range(len(productions[s])):
            if productions[s][rid] == None:
                continue
            if type(productions[s][rid]) == type(list()):
                productions[s][rid] = "".join(productions[s][rid])
            productions[s][rid] = [*productions[s][rid]]
            for i in range(len(productions[s][rid])-1,-1,-1):
                if productions[s][rid][i][0] == "'":
                    productions[s][rid][i-1]+="'"
                    productions[s][rid].pop(i)

# getting Production rules
for line in file:
    production = line.split("->")
    current_symbol = production[0]

    # setting the first Symbol as startSymbol
    if startSymbol == "":
        startSymbol = current_symbol

    rules = production[1].split("\n")[0].split('/')
    symbols.append(current_symbol)
    productions[current_symbol] = rules

    # print the production and its length
    print(current_symbol,productions[current_symbol])

parseSymbols(symbols, productions)

# getting Start Symbol of the grammar
startSymbol = input("Start symbol: ") if "y" in input("Custom Start Symbol (y/n): ").lower() else startSymbol
if startSymbol not in symbols:
    raise Exception(ValueError("Invalid Start Symbol"))


print(productions, startSymbol, symbols)

initial_productions = []
loop = 0

while productions != initial_productions and loop < 5:
    print(loop)
    loop += 1
    initial_productions = productions.copy()
    for s in symbols:
        # if symbol 's' has only 1 rule the skip to next symbol
        if len(productions[s]) < 2:
            continue

        j=1
        # get the prodution that is common in rules
        ind = 0
        while productions[s][ind] == None:
            ind+=1
        common = "".join(productions[s][ind])[:j]

        # create new symbol s' for new productions
        newSymbol = s+"'"
        while newSymbol in symbols:
            newSymbol += "'"

        symbols.append(newSymbol)
        productions[newSymbol] = []
        popInds = []

        for prodNo in range(len(productions[s])):
            prod = productions[s][prodNo]
            if prod == None:
                continue
            if prod[0] == None:
                continue
            prod = "".join(prod)
            if common == prod[:j]:
                if len(prod) <2:
                    productions[newSymbol].append(None)
                else:
                    productions[newSymbol].append(prod[j:])
                popInds.append(prodNo)
        
        productions[s].append(common+newSymbol)

        for i in range(len(popInds)):
            productions[s].pop(popInds[i] - i)

        parseSymbols(symbols, productions)


for i in productions:
    print(i +"\t", productions[i])