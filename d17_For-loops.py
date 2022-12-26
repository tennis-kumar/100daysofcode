# Day 17

# introduction to loops

# 1. For loop
# 2. While loop

# for loops are used to iterate over a sequence (list, tuple, string) or other iterable objects

# name = 'Harry'
# for i in name:
#     print(i)
#     if i == 'a':
#         print('This is something Special')

# colors = ["Red","Green","Blue","Yellow"]
# for color in colors:
#     print(color)
#     for i in color:
#         print(i)

# # range function
# for k in range(2000): # range 0 - 1999
#     print(k)

# for k in range(1,50): # range 1 - 49 syntax : range(start,stop)
#     print(k)

for k in range(1,50,2): # range 1 - 49 syntax : range(start,stop,step)
    print(k) #step is used to specify offset, ex -> i+2,i+2,i+2, here we can specify 2 in the place of step