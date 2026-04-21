# SET-2

s = input("Enter string: ")

# 1. Only allowed characters
for ch in s:
    if ch not in ['a', ',', '(', ')']:
        print("Rejected")
        exit()

# 2. Balanced parentheses
count = 0
for ch in s:
    if ch == '(':
        count += 1
    elif ch == ')':
        count -= 1
    if count < 0:
        print("Rejected")
        exit()

if count != 0:
    print("Rejected")
    exit()

# 3. Basic invalid patterns
if ",)" in s or "(," in s or s.endswith(','):
    print("Rejected")
else:
    print("Accepted")

# Odd binary
s = input().strip()
print("Odd" if s[-1]=='1' else "Even")
