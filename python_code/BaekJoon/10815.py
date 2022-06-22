N = int(input())
num_input = list(map(int, input().split()))
M = int(input())
num_differ = list(map(int, input().split()))

list_bool = []

for i in range(len(num_differ)):
    for j in range(len(num_input)):
        if num_differ[i] == num_input[j]:
            list_bool.append(1)
        elif i == len(num_differ) - 1:
            list_bool.append(0)

print(num_differ)