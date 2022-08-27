# Non deterministic grammar to deterministic grammar converions

# Global variables:
productions = {}    # store produtions rules {symbols: rules} eg. A->a/b is stored as {"A":["a","b"]}
symbols = []        # variable ie non terminal symbols
terminals = []      # terminals

print("Type 'epsilon' for epsilon production")
print("Enter Non-Deterministic Grammar: ")
line = input()

# getting Production rules
while ":wq" not in line:
    production = line.split("->")
    print(production)
    current_symbol = production[0]
    rules = production[1].split("/")
    symbols.append(symbols)
    productions[current_symbol] = rules
    line = input()

# getting Start Symbol of the grammar
startSymbol = input("Start symbol: ")

print(productions, startSymbol)