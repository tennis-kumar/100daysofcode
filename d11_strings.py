#Day 11 

# Strings in python

name = "Tennis"
friend = "Roopesh"
anotherFriend = 'Vamsi'

apple = 'Hello " double quote '

print(apple)

bc = '''This is a multiline string
should always be inside triple quotes
else error pops up'''


#String slicing

print(name[0]) #returns the first character in the string
print(name[1]) #returns the second character in the string

for character in name:
    print(character)

print(name[0:3]) #returns the first 3 characters in the string
print(name[1:3]) #returns the from the second character till the 3-1th character