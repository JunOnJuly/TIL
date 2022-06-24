N = int(input())
num_input = list(map(int, input().split()))
M = int(input())
num_differ = list(map(int, input().split()))

list_bool = []

for i in range(len(num_differ)):
    if num_differ[i] in num_input:
        list_bool.append(1)
    else:
        list_bool.append(0)

print(list_bool)