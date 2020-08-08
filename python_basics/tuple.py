# Tuple
# immutable lists

my_tuple = (1, 2, 3, 4, 5)
print(5 in my_tuple)


user = {
    'basket': [1, 2, 3],
    'greet': 'hello',
    'age':20
}

print(user.items())
# you can see the key/value pairs are tuples

new_tuple = my_tuple[1:2]
print(new_tuple)
#tuples with single items are in the form (#,)

# counts how many elements in the tuple
print(my_tuple.count(5))

#len()
print(len(my_tuple))