N = int(input())
A = sorted(list(zip(list(range(N)), list(map(int, input().split())))), key=lambda x: x[1])
P = [0 for _ in range(N)]

for i, (j, num) in enumerate(A):
    P[j] = i

print(*P)