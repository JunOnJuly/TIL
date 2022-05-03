N, Q = map(int, input().split())

usados = [list(map(int, input().split())) for i in range(N - 1)]
questions = [list(map(int, input().split())) for i in range(Q)]

map_straight = [[] for i in range(N + 1)]

stack = []

