# Variables and Data types

a = 121355555555555555551 #numbers

print(a)
Harry = 9  #number

b = "Harry" # String

print(b)

# print(a + b)  #this wont work as we can't combine integer value with string


print("The type of a is ",type(a))  # type() function will give you the type of object
print("The type of b is ",type(b))

c = complex(8 ,2)  # complex() function used to get a complex number 'a + ib format'
print(c)

d = None

print(d)
print(type(d))

e = True
print(e)
print(type(e))

#available data types in python
# 1. Numbers
# 2. String - collection of characters
# 3. List - colllection of different data elements
# 4. Tuple - tuples are immutable, collection of values, minimum 2 values needed to form a tuple
# 5. Dictionary - collection of key : value pairs
# 6. Set - a collection
# 7. Boolean - True/False
# 8. Complex - realnumbers and imaginery numbers

list1 = [8, 2.2, [5,6],['apple','banana']]   # a list
print(list1)

tuple1 = (('parrot','sparrow'),('Lion','Tiger'))  # a tuple
print(tuple1)

dict1 = {'name':'Tennis','age': 21,'canVote':True}  # a dictonary
print(dict1)

set1 = {1,2,3,4,5,6,7,8,9,10}  # a set
print(set1)