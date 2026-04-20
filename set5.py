# SET-5

# contains aaa
s = input().strip()
print("Accepted" if "aaa" in s else "Rejected")

# FIRST function
productions = []
result = set()

def FIRST(c):
    if not c.isupper():
        result.add(c)
        return
    for p in productions:
        if p[0] == c:
            rhs = p[3:]
            i = 0
            while i < len(rhs):
                if rhs[i] == '|':
                    i += 1
                    continue
                if rhs[i] == 'e':
                    result.add('e')
                    break
                if not rhs[i].isupper():
                    result.add(rhs[i])
                    break
                FIRST(rhs[i])
                if 'e' not in result:
                    break
                else:
                    result.discard('e')
                    if i+1 >= len(rhs) or rhs[i+1] == '|':
                        result.add('e')
                i += 1

n = int(input())
for _ in range(n):
    productions.append(input().strip())

symbol = input().strip()
FIRST(symbol)
print("FIRST =", result)
