# Day 25
# Operations on Tuples

# Tuples are immutable, meaning they cannot be changed
# But there are some operations that can be performed on tuples

# IF you want to add, remove or change items in tuple then first you have to convert the tuple to list
# then perform desired operation on the list and then convert list back to tuple

countries = ("Spain", "Germany", "Italy", "India", "England")

temp = list(countries)
temp.append("France")
temp.pop(4)
temp[0] = "Sri Lanka"
countries = tuple(temp)
print(countries)

tuple1 = (0,1,2,3,5,6,7,2,3,5,1,3,6,5)
print(tuple1.count(5)) # returns number of times 5 is present in tuple

print(tuple1.index(5)) # returns index of first occurence of 5 in tuple
# Raises a ValueError if the element is not present inside the tuple

res = tuple1.index(3,4,8) # will slice tuple from 4:8 and returns the index of 3 in sliced tuple
print(res)