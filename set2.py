# SET-2

inp = input().strip()
i = 0

def S():
    global i
    if i < len(inp) and inp[i] == 'a':
        i += 1
    elif i < len(inp) and inp[i] == '(':
        i += 1
        L()
        if i < len(inp) and inp[i] == ')':
            i += 1
        else:
            print("Error")
    else:
        print("Error")

def L():
    global i
    S()
    while i < len(inp) and inp[i] == ',':
        i += 1
        S()

S()
print("Accepted" if i == len(inp) else "Rejected")

# Odd binary
s = input().strip()
print("Odd" if s[-1]=='1' else "Even")
