names = "Tennis kumar"
#String Slicing and Indexing

print(names[0:5])  #print all characters from index 0 to 4 (5-1), "Including 0 and exculding 5"

#Output: Tennis

print(names[:5]) #print all characters from index starting to 4 (5-1)

print(len(names)) # print length of string, len() is a built-in function

print(names[7:]) #print all characters from index 7 to end

print(names[-1]) #print last character

print(names[-5:-1]) #print all characters from index -5 to -1 (excluding -1)

print(names[-1:]) #print all characters from index -1 to beginning


# looping through string

for i in names:
    print(i)