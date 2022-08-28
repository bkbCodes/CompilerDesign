# Non deterministic grammar to deterministic grammar converions

# Global variables:
filename = "NDG_to_DG/Grammar"    # file to be read
file = open(filename)   # open the specified file and read the Grammar
productions = {}        # store produtions rules {symbols: rules} eg. A->a/b is stored as {"A":["a","b"]}
symbols = set()            # variable ie non terminal symbols
terminals = set()          # terminals
startSymbol = ""
maxlen = 0

# getting Production rules
print("Given Grammar:")
for line in file:
    production = line.split("->")
    current_symbol = production[0]

    # setting the first Symbol as startSymbol
    if startSymbol == "":
        startSymbol = current_symbol

    [terminals.add(i) if (i>='a' and i<='z') or ord(i)-ord('a') in [range(10)] else "" for i in production[1]]
    rules = production[1].split("\n")[0].split('/')
    symbols.add(current_symbol)
    productions[current_symbol] = rules
    
    for i in range(len(rules)):
        if rules[i] == "epsilon" or rules[i] == "":
            rules[i] = None

    maxlen = max(maxlen, max([len(i) if i != None else 0 for i in rules]))
    # print the production and its length
    print(current_symbol,productions[current_symbol])


# getting Start Symbol of the grammar
startSymbol = input("Start symbol: ") if "y" in input("Custom Start Symbol (y/n): ").lower() else startSymbol
if startSymbol not in symbols:
    raise Exception(ValueError("Invalid Start Symbol"))


newSymbols = set()
first = 1
ignoreList = []
initial_productions = []

while (newSymbols != set() or first == 1) and initial_productions != productions:
    first += 1
    newSymbols = set(())
    initial_productions = productions.copy()
    for s in symbols:
        if s[0] in ignoreList:
            continue
        # if symbol 's' has only 1 rule the skip to next symbol
        if len(productions[s]) < 2:
            if productions[s][0] == None:
                ignoreList.append(s[0])
            continue
        
        j=1
        # get the prodution that is common in rules
        ind = 0
        while productions[s][ind] == None:
            ind += 1
        common = productions[s][ind][:j]

        # create new symbol s' for new productions
        newSymbol = s+"'"
        newSymbols.add(newSymbol)
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
    symbols = symbols.union(newSymbols)
    print(productions)


print("Deterministic Grammar:")
for i in productions:
    print(i +"\t", productions[i])