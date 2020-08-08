basket = [1, 2, 3, 4, 5]


# Append
# should print 5
new_list = basket.append(100)

# appended with 100 ( 1, 2, 3, 4, 5, 100)
print(basket)

# prints nothing
print(new_list)

# to fix this, we can do 
new_list = basket

print(new_list)

#Insert
basket.insert(5, 100)
print(basket)

# Extend
basket.extend([100, 101])
print(basket)

#removing
# removes a 4
basket.remove(4)

#pops from the back
basket.pop()

# returns the 4th element and pops it out of the list
basket.pop(4)
print(basket)

#clear
basket.clear()

basket = ['a', 'b', 'c', 'd', 'e']

# where is the index of 'd' from [index 0 to index 4) 
print(basket.index('d', 0, 4))


# returns True if in list
print('d' in basket)
print('i' in 'hi my name is Ian')

# prints how many times 'd' occurs in the list
print(basket.count('d'))

# sort
basket = ['a', 'x', 'b', 'c', 'd', 'e']
basket.sort()
print(basket)

# sorted, creates a new copy of basket
basket = ['a', 'x', 'b', 'c', 'd', 'e']
print(sorted(basket))
print(basket)

# reverse
basket.reverse()
print(basket)
print(sorted(basket))

# slice it
print(basket[::-1])
print(basket)

print(list(range(101)))

new_sentence = ' '.join(['hi', 'my', 'name', 'is', 'jo'])

print(new_sentence)