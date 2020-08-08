#reduce
from functools import reduce

#maps
my_list = [1, 2, 3]
def multiply_b2(item):
    return item * 2

print(list(map(multiply_b2, my_list)))
print(my_list)

#filter

def check_odd(item):
    return item % 2 != 0

print(list(filter(check_odd, my_list)))
print(my_list)

#zip
your_list = [10, 20, 30]
their_list = [4, 3, 2]
print(list(zip(my_list, your_list, their_list)))

def accumulator(acc, item):
    print(acc, item)
    return acc + item
#reduce
print(reduce(accumulator, my_list, 0))