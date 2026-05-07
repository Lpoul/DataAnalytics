
side_a = eval(input("Please enter side a for a rectangle: "))
side_b = eval(input("Please enter side b for the recatangle: "))
area_rectangle = side_a * side_b

print(f"Side A is {side_a}")
print(f"Side B is {side_b}")
print(f"The area of the rectangle is {area_rectangle}")

# Some pit-falls that might happen when using the input is not have the answer data type being what you wanted. I was able to fix this by assigning the value type with eval. 
