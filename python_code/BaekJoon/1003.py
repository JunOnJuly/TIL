# 피보나치 함수 정의
def fibonacci(num: int):
    if num == 0:
        call_0.append(0)
        return 0
    elif num == 1:
        call_1.append(1)
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


# 데이터 입력
test_time = int(input())
num_list = []
for i in range(test_time):
    num_list.append(int(input()))

# 출력
for i in num_list:
    call_0 = []
    call_1 = []
    fibonacci(i)
    print("{0} {1}".format(len(call_0), len(call_1)))