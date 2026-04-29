
grammar = {
    'E': ['TR'],
    'R': ['+TR', 'e'],
    'T': ['FY'],
    'Y': ['*FY', 'e'],
    'F': ['(E)', 'id']
}

def first(symbol):
    result = set()

    if not symbol.isupper():
        return {symbol}

    for prod in grammar[symbol]:
        if prod == 'e':
            result.add('e')
        else:
            result |= first(prod[0])

    return result

for nt in grammar:
    print("FIRST(", nt, ") =", first(nt))