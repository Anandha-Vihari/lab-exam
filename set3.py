# SET-3

inp = input().strip()
i = 0

def E():
    T()
    Eprime()

def Eprime():
    global i
    if i < len(inp) and inp[i] == '+':
        i += 1
        T()
        Eprime()

def T():
    F()
    Tprime()

def Tprime():
    global i
    if i < len(inp) and inp[i] == '*':
        i += 1
        F()
        Tprime()

def F():
    global i
    if i < len(inp) and inp[i] == '(':
        i += 1
        E()
        if i < len(inp) and inp[i] == ')':
            i += 1
        else:
            print("Error")
    elif i+1 < len(inp) and inp[i]=='i' and inp[i+1]=='d':
        i += 2
    else:
        print("Error")

E()
print("Accepted" if i == len(inp) else "Rejected")

# 3rd from right is 'a'
s = input().strip()
print("Accepted" if len(s)>=3 and s[-3]=='a' else "Rejected")
