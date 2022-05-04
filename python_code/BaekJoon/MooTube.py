N, Q = map(int, input().split())

usados = [list(map(int, input().split())) for i in range(N - 1)]
questions = [list(map(int, input().split())) for i in range(Q)]

map_straight = usados[::]

while True:
    if not usados:
        break

    stack = [usados.pop()]

    while True:

