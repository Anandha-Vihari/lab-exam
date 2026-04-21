# SET-1
# Correct FIRST implementation (no global bugs)

productions = {}

def add_production(line):
    lhs, rhs = line.split("->")
    productions[lhs] = rhs.split("|")


def FIRST(symbol):
    result = set()

    # If terminal → return directly
    if not symbol.isupper():
        return {symbol}

    # For each production of symbol
    for prod in productions[symbol]:

        i = 0
        while True:
            # Case 1: epsilon
            if prod[i] == 'e':
                result.add('e')
                break

            # Case 2: terminal
            if not prod[i].isupper():
                result.add(prod[i])
                break

            # Case 3: non-terminal
            temp = FIRST(prod[i])
            result |= (temp - {'e'})   # add everything except epsilon

            if 'e' in temp:
                i += 1
                if i >= len(prod):
                    result.add('e')
                    break
            else:
                break

    return result


# -------- MAIN --------
n = int(input("Enter number of productions: "))

for _ in range(n):
    line = input().strip()
    add_production(line)

symbol = input("Enter symbol: ").strip()

ans = FIRST(symbol)
print("FIRST =", ans)

# Even binary
s = input().strip()
print("Even" if s[-1]=='0' else "Odd")
