def in_order(v):
    if v <= N:
        in_order(v * 2)
        tree[v] = max(tree) + 1
        in_order(v*2 + 1)


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    tree = [0] * (N+1)

    in_order(1)

    print(f'#{tc} {tree[1]} {tree[N//2]}')