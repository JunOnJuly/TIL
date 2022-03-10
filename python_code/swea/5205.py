def quick_sort(data_list):  # 리스트 자체를 퀵소트
    def sort(low, high):  # 리스트를 소트
        if high <= low:  # 리스트의 길이가 1 혹은 2 면 끝
            return

        mid = partition(low, high)  # 자르는 기준 설정
        sort(low, mid - 1)  # mid 기준으로 왼쪽
        sort(mid, high)  # mid 기준으로 오른쪽

        # 두 개로 나누기

    def partition(low, high):  # 자르는 기준 결정하는 함수
        pivot = data_list[(low + high) // 2]  # pivot

        while low <= high:  # low 와 high 가 일치할 때 까지
            while data_list[low] < pivot:  # pivot 보다 작으면 + 1
                low += 1
            while data_list[high] > pivot:  # pivot 보다 크면 -1
                high -= 1
            if low <= high:  # 두개 위치 변경
                data_list[low], data_list[high] = data_list[high], data_list[low]
                low, high = low + 1, high - 1
        return low  # low 와 high 가 일치한 위치 리턴

    return sort(0, len(data_list) - 1)


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    data_input = list(map(int, input().split()))

    quick_sort(data_input)
    print(f'#{tc} {data_input[N//2]}')
