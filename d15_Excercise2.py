# Day 15

# Excercise 2

# Program that greets the user based on the time of the day

import time

local_time = time.strftime("%H:%M:%S")
print(local_time)

if (local_time >= '00:00:00' and local_time < '12:00:00'):
    print('Good Morning')
elif (local_time >= '12:00:00' and local_time < '18:00:00'):
    print('Good Afternoon')
else:
    print('Good Evening')