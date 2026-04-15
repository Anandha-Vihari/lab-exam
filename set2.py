# SET-2

input_str = input().strip()
i = 0

def S():
    global i
    if i < len(input_str) and input_str[i] == 'a':
        i += 1
    elif i < len(input_str) and input_str[i] == '(':
        i += 1
        L()
        if i < len(input_str) and input_str[i] == ')':
            i += 1
        else:
            print("Error")
    else:
        print("Error")

def L():
    global i
    S()
    while i < len(input_str) and input_str[i] == ',':
        i += 1
        S()

S()
print("Accepted" if i == len(input_str) else "Rejected")

# Even/Odd binary
s = input().strip()
print("Even" if s[-1]=='0' else "Odd")
