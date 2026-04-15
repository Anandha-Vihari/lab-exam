# SET-4

s = input().strip()

# Ends with 00
print("Accepted" if len(s)>=2 and s[-1]=='0' and s[-2]=='0' else "Rejected")

# Odd binary
print("Odd" if s[-1]=='1' else "Even")
