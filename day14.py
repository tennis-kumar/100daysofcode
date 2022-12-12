# Day 14

# If ELse conditional statements

a = 18
print('Your age is: ',a)

# Conditional operators

# >, <, >=, <=, ==, !=

# print(a>18)
# print(a<18)
# print(a>=18)
# print(a<=18)
# print(a==18)
# print(a!=18)

if a>=18:
    print('Yes')
    print('You can drive')
else:
    print('No')
    print('You cannot drive')
print('Yay!!!') #Indentation is important in Python

applePrice = 210
budget = 200

if applePrice <= budget:
    print('Alexa, add 1kg Apples to cart.')
else:
    print('Alexa,do not add to cart.')

# Nested if else

num = int(input('Enter the value of num: '))

if num<0:
    print('Negative')
elif num < 0:
    if num == 999:
        print('Number is Special')
    else:
        print('Positive')
else:
    print('Number is Zero')

print('I am happy now')
