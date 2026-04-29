
s = "baaaab"
state = 0

for ch in s:
    if state == 0:
        state = 1 if ch == 'a' else 0
    elif state == 1:
        state = 2 if ch == 'a' else 0
    elif state == 2:
        state = 3 if ch == 'a' else 0
    elif state == 3:
        state = 3

print("Accepted" if state == 3 else "Rejected")