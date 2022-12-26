# Day 23
# List Methods

l = [11,36,54,4,62,7,29]
print(l)

# append() : adds an item to the end of the list

l.append(8)
print(l)

# insert() : insert an item at a particular index

l.insert(2, 100)
print(l)

# sort() : sort the list

l.sort()
print(l)

# sort in descending order
l.sort(reverse=True)
print(l)

# reverse() : reverse the list

l.reverse()
print(l)

# index() : returns the index of the first occurrence of the item

print(l.index(62))

# count() : count the no of occurrences of that particular value

print(l.count(11))


m = l # m will be a reference of l in the memory and not a copy
print(m)
m[0] = 0 # value at index 0 will be set to 0 in both the lists

print(l)
print(m)

# copy() : copy the list

n = l.copy() # create a seperate copy of the list
print(n)
n[0] = 100 # value at index 0 will be set to 100 in n and not in l
print(l)

# extend() : similar to string concatenation 

k = [256,52,96,4,0,1,353]
l.extend(k) # values of k will be added to the end of l
print(l)