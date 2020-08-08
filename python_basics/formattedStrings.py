# formatted strings

name = 'Johnny'
age = 55

print('hi ' + name + '. You are ' + str(age) + ' years old')

# you can add f after print
print(f'hi {name}. You are {age} years old')

# or you can add .format after orubt
print('hi {new_name}. You are {age} years old'.format(new_name='sally', age=100))