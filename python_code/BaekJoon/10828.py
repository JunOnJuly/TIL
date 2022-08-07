import sys

N = int(sys.stdin.readline().rstrip())
stack = []

for _ in range(N):
    order = sys.stdin.readline().rstrip()

    if 'push' in order:
        stack.append(order.split(' ')[1])
    elif order == 'pop':
        if stack:
            print(stack[-1])
            stack = stack[:-1]
        else:
            print(-1)
    elif order == 'size':
        print(len(stack))
    elif order == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    else:
        if stack:
            print(stack[-1])
        else:
            print(-1)