
s = "(a,a)"
i = 0

def S():
    global i
    if i < len(s) and s[i] == 'a':
        i += 1
        return True

    if i < len(s) and s[i] == '(':
        i += 1
        if L() and i < len(s) and s[i] == ')':
            i += 1
            return True

    return False

def L():
    global i

    if not S():
        return False

    while i < len(s) and s[i] == ',':
        i += 1
        if not S():
            return False

    return True

print("Accepted" if S() and i == len(s) else "Rejected")