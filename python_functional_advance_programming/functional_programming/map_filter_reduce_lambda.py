from functools import reduce

print(list(map(lambda x: x * 2, [23, 34, 45])))

print(list(filter(lambda x: x % 2 == 0, [23, 34, 45])))


def reduce_sum(acc, iter_item):
    return acc + iter_item


print(reduce(reduce_sum, [34, 45, 56]))
