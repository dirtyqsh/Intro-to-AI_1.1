def more_than_five(lst):
    new_lst = []
    for i in lst:
        if abs(i) > 10:
            new_lst.append(i)
    return new_lst