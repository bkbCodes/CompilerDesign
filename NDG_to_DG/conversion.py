# Non deterministic grammar to deterministic grammar converions

# Global variables:
filename = "NDG_to_DG/Grammar"    # file to be read
file = open(filename)   # open the specified file and read the Grammar
productions = {}        # store produtions rules {symbols: rules} eg. A->a/b is stored as {"A":["a","b"]}
symbols = []            # variable ie non terminal symbols
terminals = []          # terminals
startSymbol = ""


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
    print(productions[current_symbol])
    print(len(productions[current_symbol]))


# getting Start Symbol of the grammar
startSymbol = input("Start symbol: ") if "y" in input("Custom Start Symbol (y/n): ").lower() else startSymbol
if startSymbol not in symbols:
    raise Exception(ValueError("Invalid Start Symbol"))


print(productions, startSymbol, symbols)


for s in symbols:
    # if symbol 's' has only 1 rule the skip to next symbol
    if len(productions[s]) < 2:
        continue

    j=1
    # get the prodution that is common in rules
    common = productions[s][0][:j]

    # create new symbol s' for new productions
    newSymbol = s+"'"
    symbols.append(newSymbol)
    productions[newSymbol] = []
    popInds = []

    for prodNo in range(len(productions[s])):
        prod = productions[s][prodNo]
        if prod == None:
            continue
        if common == prod[:j]:
            if len(prod) <2:
                productions[newSymbol].append(None)
            else:
                productions[newSymbol].append(prod[j:])
            popInds.append(prodNo)
    
    productions[s].append(common+newSymbol)

    for i in range(len(popInds)):
        productions[s].pop(popInds[i] - i)


for i in productions:
    print(i +"\t", productions[i])