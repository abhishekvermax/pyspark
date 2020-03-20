def curry_add(x):
    def add_item_1(y):
        def add_item_2(z):
            return x + y + z

        return add_item_2

    return add_item_1

add_item1 = curry_add(1)(2)
print(add_item1(7))
print(curry_add(1)(2)(3))
