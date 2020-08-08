# len()
greet = 'hellloooo'
#prints from the start to the length of greet
print(greet[0:len(greet)])

# upper()
# prints uppercase of quote
quote = 'to be or not to be'
print(quote.upper())

# capitalize()
print(quote.capitalize())

# find()
print(quote.find('be'))

# replace()
print(quote.replace('be', 'me'))

# even tho we use replace(), we do not change the original string
# we never modify it because it is immutable
print(quote)