# Day 19

# Break and continue

# Day 18 task - do while loop emulation
# emulation of do while loop using break 

# S_word = 'Python'
# counter = 0

# while True:
#     word = input('Enter the secret word: ').lower()
#     counter += 1
#     if word == S_word:
#         break
#     if word != S_word and counter > 3:
#         print('You have exceeded the number of attempts')
#         break

# Day 19 progress from here

# Break and continue

# Break - breaks out of the loop / terminates the loop
# Continue - skips the current iteration and continues with the next iteration

for i in range(12):
    if i == 10:
        print('Skip the iteration')
        continue
    print('5 X',i,' = ',5 * i)