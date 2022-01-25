def warp(num_input: int) -> int:
    num_str = '1 2 3'
    for i in range(num_input - 3):
        num_str = num_str + f' {int(num_str.split()[-1])+int(num_str.split()[-2])-2}'
    return int(num_str.split()[-1])


# 데이터 입력
test_num = int(input().strip())
for i in range(test_num):
    num1, num2 = map(int, input().split())
    num = num2 - num1
    print(warp(num))