# Day 24

# Tuples in Python
# Tuples are ordered collection of data items, similar to lists
# Tuple items are enclosed within (  ) braces and seperated by ,
# Tuples are immutable, meaning they cannot be changed

# Tuples are used to store multiple items in a single variable

tup = (1,5,6)
print(type(tup),tup)

# if tuple contains only one element need to follow below format
tup1 = (1,)
print(type(tup1),tup1)

# Tuple can contain different data types
tup2 = (1,2.5,"Hello")

# Tuple can contain another tuple
tup3 = (1,2.5,"Hello",(1,2,3))
print(tup3)

# Tuple can contain list
tup4 = (1,2.5,"Hello",[1,2,3],247)
print(tup4)

print(len(tup4)) # returns length of the tuple

print(tup4[0]) #returns value at 0th index
print(tup4[0:2]) # returns values from 0th index to 2nd index
print(tup4[0:]) # returns values from 0th index to last index

if 247 in tup4:
    print("Found")
else:
    print("Not Found")

if 2471 in tup4:
    print("Found")
else:
    print("Not Found")

# Slicing can be done on Tuples, but the result will be a new tuple
tup5 = tup4[0:2]
print(tup5)