def sorting():
    return 0


N = int(input())
num_list = [int(input()) for _ in range(N)]

sorted_list = sorting(num_list)

for num in sorted_list:
    print(num)