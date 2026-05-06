
name = "Hello"

print(f"Original string : {name}")


print(f"Original string : {name[0]}")

# name[0] = "J"

string = 'Hello, World!'
print(string[0])
print(string[-1])
print(string[1:4])

print(string.split(','))

string = "Hello, World!"

# Convert to uppercase
print(string.upper())  # Output: HELLO, WORLD!

# Find a substring
print(string.find("World"))  # Output: 7

# Replace a substring
print(string.replace("World", "Python"))  # Output: Hello, Python!

# Split a string
print(string.split(","))  # Output: ['Hello', ' World!']

f_name =  "Jordan Worrabah" 
s_name = "Lilly Wells"
t_name = "Jonathan Lopez"

print(f_name+ ", \n"+s_name+", \n"+t_name)


# \'        -> single quote
# \n        -> newline
# \r        -> carriage return
# \t        -> tab
# \b        -> backspace
# \f        -> formfeed
# \ooo      -> octal value
# \xhh      -> hex value
# \\        -> backslash
# \uxxxx    -> 16‑bit hex value
# \uxxxxxxxx -> 32‑bit hex value



import math
print(f"{math.pi:.2f}") 


from math import pi
print(f"{pi:.2f}")  


# Deodat P. Sharma
# 4/28/2026
# user input in python

# Ask the user to enter two numbers
int num1 = input("Enter the first number: ")
int num2 = input("Enter the second number: ")

print(f'You have entered {num1} and {num2}')

print(type(num1))
print(type(num2))

print(f'The sum of {num1} and {num2} is {num1 + num2}')
print(f'The product of {num1} and {num2} is {num1 * num2}')
print(f'The product of 2 and {num2} is {2 * num2}')
