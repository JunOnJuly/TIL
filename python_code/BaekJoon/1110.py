# 데이터 입력
N = int(input())

# 계산
list_nums = [N]
while True:
    if N < 10:
        N = int(str(N)[-1] + str(int(str(N * 10)[0]) + int(str(N * 10)[-1]))[-1])
    else:
        N = int(str(N)[-1] + str(int(str(N)[0]) + int(str(N)[-1]))[-1])
    if N in list_nums:
        break
    list_nums.append(N)

print(len(list_nums))