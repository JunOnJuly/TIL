import math

A, B, C = map(int, input().split())

if C <= B:
    print(-1)
else:
    print(math.floor(A/(C-B) + 1))