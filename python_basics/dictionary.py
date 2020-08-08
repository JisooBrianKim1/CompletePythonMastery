# letters are keys, and numbers are values
# dictionary elements must be unique else we overwrite
dictionary = {
    'weapons': [1,2,3],
    'greeting': 'hello',
    'is_Magic': True
}

dictionary = {
    123: [1,2,3],
    True: 'hello',
    # [100]: True
}

print(dictionary[123])
print(dictionary[True])

# does not print True because [100] which is a list is mutable
#print(dictionary[100])

# Dictionary Methods
user = {
    'basket': [1, 2, 3],
    'greet': 'hello'
}

# if 'age' does not exist, return 55
print(user.get('age', 55))

# another way to create dictionaries
user2 = dict(name = 'John')
print(user2)

print('basket' in user)

print('greet' in user.keys())
print('hello' in user.values())

print(user.items())

print(user.clear())
# you can also do user.clear() and print(user)

user = {
    'basket': [1, 2, 3],
    'greet': 'hello'
}

user2 = user.copy()
print(user.clear())
print(user2)

user = {
    'basket': [1, 2, 3],
    'greet': 'hello'
}

#popitem
# pops off some pair in the dictionary, NOT THE LAST ONE
print(user.popitem())

#update
print(user.update({'age': 55}))
print(user)