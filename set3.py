s = input("Enter expression: ")

# 1. Replace 'id' with single symbol
s = s.replace("id", "x")

# 2. Check valid characters
for ch in s:
    if ch not in ['x', '+', '*', '(', ')']:
        print("Rejected")
        exit()

# 3. Check parentheses balance
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

# 4. Invalid patterns
invalid = ["++", "**", "+*", "*+", "(+", "(*", "+)", "*)"]

for p in invalid:
    if p in s:
        print("Rejected")
        exit()

# 5. Cannot start/end with operator
if s[0] in ['+', '*'] or s[-1] in ['+', '*']:
    print("Rejected")
    exit()

print("Accepted")

# 3rd from right is 'a'
s = input().strip()
print("Accepted" if len(s)>=3 and s[-3]=='a' else "Rejected")
