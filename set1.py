# SET-1

# FIRST Function
productions = []
result = []

def find_first(c):
    if not c.isupper():
        result.append(c)
        return
    for p in productions:
        if p[0] == c:
            if p[2] == '#':
                result.append('#')
            else:
                find_first(p[2])

n = int(input())
for _ in range(n):
    productions.append(input())

symbol = input().strip()
find_first(symbol)

print("FIRST(", symbol, ") = {", " ".join(result), "}")

# Even binary
s = input().strip()
print("Even" if s[-1]=='0' else "Odd")
