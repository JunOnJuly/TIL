def my_all(iter_args):
    bool_list = list(map(bool, [i for i in iter_args]))
    print(bool_list)
    for bool_item in bool_list:
        if bool_item:
            continue
        else:
            return False
    return True
