import re
pattern = re.compile('search inside of this text please!')
string = 'search inside of this text please! Andrei'

# returns a match object or NONE
a = pattern.search(string)
b = pattern.findall(string)
c = pattern.fullmatch(string)
d = pattern.match(string)
print(a.group())
print(b)
print(c)
print(d)