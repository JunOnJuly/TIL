# 피보나치 함수 정의
fib_num = []
fib_num.append(0)
fib_num.append(1)
for i in range(39):
    fib_num.append(fib_num[i] + fib_num[i + 1])


# 데이터 입력
test_time = int(input().strip())

for i in range(test_time):
    input_num = int(input().strip())
    if input_num == 0:
        print(f'{1} {0}')
    else:
        print(f'{fib_num[input_num - 1]} {fib_num[input_num]}')