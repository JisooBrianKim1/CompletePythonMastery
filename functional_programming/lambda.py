from functools import reduce

my_list = [1, 2, 3]

def check_odd(item):
    return item % 2 != 0

#multiplies by 2
#lambda param: action(param)
print(list(map(lambda item: item * 2, my_list)))

# accumulator
print(reduce(lambda acc, item: acc+item, my_list))
print(my_list)