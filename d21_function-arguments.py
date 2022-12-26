# Day 21

# Function arguments in python

# def average(a, b):
#     print('The average is ', (a+b)/2)

# average(4, 6)

# 4 types of arguments :

    # 1. Required arguments
# def average(a = 3, b = 4):
#     print('The average is ', (a+b)/2)

# average()

    # 2.Default arguments
def name(fname, mname = 'John', lname = 'Doe'):
    print('Hello', fname, mname, lname)

name('John', 'Doe')  # -> o/p: Hello John Doe Doe  , here default mname is overridden by 'Doe'

    # 3.Keyword arguments
def name1(fname, mname, lname):
    print('Hello', fname, mname, lname)

name1(mname= 'Peter', lname = 'Wesker', fname='Jade') # -> o/p: Hello Jade Peter Wesker, here order of arguments doesn't matter

    # 4. Variable length arguments

    # can pass any number of arguments, but they are stored in a tuple

def average(*b):
    c = 0
    for i in b:
        c += i
    print(c)
    print('Average is ', c/len(b))
    #return c/len(b)
    #return 7             -> the first return statement is executed

c = average(1, 2, 3, 4, 5, 6, 7, 8, 9, 10) # -> o/p: 55
print(c) # -> o/p: None without return statement

def person(name, **data): # -> **data stores the arguments in a dictionary
    print(name)
    for i, j in data.items():
        print(i, j)

person('John', age = 22, city = 'New York', mob = 1234567890) # -> o/p: John age 22 city New York mob 1234567890