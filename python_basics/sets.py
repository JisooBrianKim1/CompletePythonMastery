# sets
#an UNOREDERED collection of UNIQUE objects

my_set = {1, 2, 3, 4, 5}
my_set.add(100)
my_set.add(2) # no duplicates

print(my_set)

my_list = [1, 2, 3, 4, 5, 5]
print(set(my_list))

print(1 in my_set)

print(len(my_set))
my_set.clear()
print(my_set) # prints out default set method; set()

my_set = {1, 2, 3, 4, 5}
your_set = {4, 5, 6, 7, 8, 9, 10}

# print(my_set.difference(your_set))
# print(my_set.discard(5))
# print(my_set)
# print(my_set.difference_update(your_set))
# print(my_set)
# print(my_set.intersection(your_set))
# can also do print(my_set & your_set)
# print(my_set.isdisjoint(your_set))
# print(my_set.union(your_set)) 
# can also do print(my_set | your_set)
# print(my_set.issubset(your_set))
# print(your_set.issuperset(my_set))
