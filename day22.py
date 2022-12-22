# Day 22

# Introduction to Lists

# List items are seperated by , and enclosed in [  ]

# Lists are a data structure in Python that is a mutable, or changeable, ordered sequence of elements. Each element or value that is inside of a list is called an item. Just as strings are defined as characters between quotes, lists are defined by having values between square brackets [ ].

# Lists can contain any mix and match of the data types that we have learned about so far.

marks = [3,5,7,"Harry",True,8,12,'Hello','Rupali',12.0,13.7]
print(marks)
print(type(marks))

# Lists can also be indexed and sliced like strings.

print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])

# Negative indexing

print(marks[-1])
print(marks[-2])
print(marks[-3])
print(marks[-4])
print(marks[-5])

# in keyword used to iterate through the list
if 7 in marks:
    print("Yes")
else:
    print("No")

# but when passed as string, returns false

if "7" in marks:
    print("Yes")
else:
    print("No")

# List Slicing, Lists can be sliced, same as strings

print(marks)
print(marks[:])
print(marks[0:3])
print(marks[1:4])
print(marks[0:-1])

print(marks[0:5:2])  # third parameter specifies the jump index i.e, how many places skip, i.e, if third param is 2, then op will be i,i+2,(i+2)+2
print(marks[0:5:3])  # here the jump index is 3, so it will print thr 3rd consecutive item


# List comprehension

lst = [i*i for i in range(10)]
print(lst)

lst2 = [i*i for i in range(10) if i%2 == 0]
print(lst2)

# example 1 : accepts items with small letter "0" in the new list

names = ["Milo","Sarah","Bruno","Anastasia","Rosa"]

nameswith_o = [item for item in names if "o" in item]
print(nameswith_o)

# example 2 : accepts items which have more than 4 letters

nameswith_4 = [item for item in names if len(item) > 4]
print(nameswith_4)