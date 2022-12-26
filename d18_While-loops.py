# Day 18 

# Introduction to While loop

# i= int(input('Enter the number: '))

# while(i<=5):   # syntax -> while (condition): stmnt
#     print(i)
#     i= int(input('Enter the number: '))
#     i+=1
# print('Done with the loop')

count = 20

while(count>0):
    print(count)
    count-=1
else:
    print('Done with the loop, i\'m inside else')

#Do while loop is not present in Python 
# need to figure out to emulate DO While loop in python