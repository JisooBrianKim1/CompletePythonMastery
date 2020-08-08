li = [1, 2, 3, 4, 5]
li2 = ['a', 'b', 'c']
li3 = [1, 2, 'a', True]

# Data Structure

amazon_cart = [
    'notebooks', 
    'sunglasses',
    'toys',
    'grapes'
]

#List slicing

print(amazon_cart[0::2])

#Lists are mutable
amazon_cart[0] = 'laptop'
print(amazon_cart[0:3])
print(amazon_cart)

#list slicing creates a new object
new_cart = amazon_cart
new_cart[0] = 'another laptop'

print(new_cart)
print(amazon_cart)

# new_cart has been modified AND amazon_cart too
# they are the same cart, they have the same memory
# think of pointers

new_cart = amazon_cart[::-1]
print(new_cart)
print(amazon_cart)