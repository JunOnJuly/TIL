1.


def list_sum(nums: list) -> int:
    sum_num = 0
    for num in nums:
        sum_num += num
    return sum_num


# -----------------------------------------------
2.


def dict_list_sum(dict_list: list) -> int:
    sum_age = 0
    for i in range(len(dict_list)):
        sum_age += dict_list[i]['age']

    return sum_age


# -----------------------------------------------
3.


def all_list_sum(all_list: list) -> int:
    sum_list = 0
    for i in range(len(all_list)):
        for num in all_list[i]:
            sum_list += num

    return sum_list