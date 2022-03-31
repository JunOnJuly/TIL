from collections import deque

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    data_input = [list(map(int, input().split())) for _ in range(N)]

    que = deque()
    