# Name: Leon Poulson
# Date: 5/11/26
# Instructor: Deodat
# Making if statements to see what time of the day it is to greet you

hour = int(input("What hour is it? (0–23): "))

if 23 >= hour or hour <= 4:
    print("What are you doing up so late??")
elif hour < 10:
    print("Good morning!")
elif hour < 17:
    print("Good day!")

else:
    print("Good evening!")