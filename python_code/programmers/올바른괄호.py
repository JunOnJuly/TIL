s = ["()()", "(())()" , ")()(", "(()("]

stack = []

for string in s[3]:
    if string == '(':
        stack.append(string)
    else:
        if stack and stack[-1] == '(':
            stack.pop()
            continue

if not stack:
    print('true')
else:
    print('false')