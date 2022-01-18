# 연속된 배열을 얼마나 많이 찾아낼 수 있는가?

# 변수 입력
num_test = int(input())

for i in range(num_test):

    n = []
    n.append(int(input()))
    print(n)
    xi_di = []
    for j in range(num_test):
        xi_di.append([])
    print(i)
    print(n[i])
    for j in range(n[i]):
        xi_di[i].append(list(map(int, input().split())))

print(num_test, n, xi_di)