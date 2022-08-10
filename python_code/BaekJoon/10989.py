import sys

N = int(sys.stdin.readline())

num_count = [0]*10001

for _ in range(N):
    num = int(sys.stdin.readline())
    num_count[num] += 1

for i in range(10001):
    if num_count[i]:
        for j in range(num_count[i]):
            print(i)