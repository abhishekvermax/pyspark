def count_up(lst, maximum):
    if lst > maximum:
        return
    print(lst)
    count_up(lst + 1, maximum)


def traverse_list(lst, i=0):
    if i < len(lst):
        traverse_list(lst, i + 1)


traverse_list([23, 45, 56])
