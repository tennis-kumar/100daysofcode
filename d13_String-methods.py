# Day 13 : String Methods

# Strings are immutable, so you can't change them in place

a  =  "Hello"
print(len(a)) # prints length of string
print(a.upper()) # prints string in upper case
print(a.lower()) # prints string in lower case
print(a.title()) # prints string in title case
print(a.count("l")) # prints number of times "l" occurs in string
print(a.find("l")) # prints index of first occurence of "l" in string
print(a.find("l", 2)) # prints index of first occurence of "l" in string after index 2

# String Formatting
b = "!!!!! Tennis !!!!!! !!!!!Tennis !!!!!"
print(b.rstrip("!")) # removes all trailing "!" from string

print(b.lstrip("!")) # removes all leading "!" from string

print(b.replace("Tennis","Kumar"))

print(b.split(" ")) # splits string into list of substrings at " " (space)

c = "introduction to python"

print(c.capitalize()) # capitalizes first letter of string

print(c.center(50, "*")) # centers string in 50 characters with "*" as padding

print(c.startswith("introduction")) # checks if string starts with "introduction"

print(c.endswith("python")) # checks if string ends with "python"

print(c.endswith("python", 0, 20)) # checks if string ends with "python" between index 0 and 20

print(c.isalnum()) # checks if string is alphanumeric

print(c.isalpha()) # checks if string is alphabetic

print(c.isdigit()) # checks if string is numeric (Integer)

print(c.islower()) # checks if string is in lower case

print(c.isupper()) # checks if string is in upper case

print(c.istitle()) # checks if string is in title case

print(c.join("abc")) # joins string with "abc"

d = "Happy Christmas\n"

print(d)

print(d.isprintable()) # checks if string is printable (returns False for \n)

e = "        "

print(e.isspace()) # checks if string is a space (returns True for " ")

f = "Happy Christmas"

print(f.istitle()) # checks if string is in title case

print(d.swapcase()) # swaps case of string (upper to lower and vice versa)

g = "His name is Daniel"

print(g.title())
