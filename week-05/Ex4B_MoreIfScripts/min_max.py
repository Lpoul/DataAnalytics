# Name: Leon Poulson
# Date: 5/11/26
# Instructor: Deodat
# Making if statements to compare numbers


num_1 = eval(input("Enter the first number: "))
num_2 = eval(input("Enter the second number: "))
num_3 = eval(input("Enter the third number: "))


if num_1 <= num_2 and num_1 <= num_3:
    smallest = num_1
elif num_2 <= num_1 and num_2 <= num_3:
    smallest = num_2
else:
    smallest = num_3


if num_1 >= num_2 and num_1 >= num_3:
    largest = num_1
elif num_2 >= num_1 and num_2 >= num_3:
    largest = num_2
else:
    largest = num_3


print(f"Smallest number: {smallest}")
print(f"Largest number: {largest}")