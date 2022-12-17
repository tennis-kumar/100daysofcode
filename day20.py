# Day 20

# functions in python
# function is a block of code which only runs when it is called

# Rules to naming a function
# 1. Function name should be in camelCase
# 2. Function name should be a verb
# 3. Function name should be short and descriptive
# 4. Function name should not be a keyword
# 5. Function name should not be a built-in function

def calculateGmean(a, b):
    mean = (a*b)/(a+b)
    print(mean)

def greaternumber(a, b):
    if a > b:
        print('First number is greater')
    else:
        print('Second number is greater')

def isLesser(a,b):
    pass

a = 9
b = 8

calculateGmean(a, b)
greaternumber(a, b)
c = 8
d = 7
# gmean2 = (c*d)/(c+d)
# print(gmean2)

calculateGmean(c, d)
greaternumber(c, d)