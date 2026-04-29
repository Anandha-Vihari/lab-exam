
s = "id+id*id"
i = 0

def E():
    return T() and EP()

def EP():
    global i
    if i < len(s) and s[i] == '+':
        i += 1
        return T() and EP()
    return True

def T():
    return F() and TP()

def TP():
    global i
    if i < len(s) and s[i] == '*':
        i += 1
        return F() and TP()
    return True

def F():
    global i

    if i + 1 < len(s) and s[i:i+2] == "id":
        i += 2
        return True

    if i < len(s) and s[i] == '(':
        i += 1
        if E() and i < len(s) and s[i] == ')':
            i += 1
            return True

    return False

print("Accepted" if E() and i == len(s) else "Rejected")