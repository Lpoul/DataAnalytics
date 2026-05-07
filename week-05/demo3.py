# Name: Leon Poulson
# Date: 5/6/2026

# name = input("Please enter your name ")
# f_num = float(input("Please enter your first number"))
# s_num = float(input("Please enter your secound number"))
# t_num = float(input("Please enter your third number"))

# avrg = float((f_num+s_num+t_num)/3)

# print(f"Hello {name}! The Average of {f_num}, {s_num},  and {t_num} is {round(avrg,2)}")

# o_price = float(input("Enter the original price: "))
# d_percent = float(input("Enter the discount percentage: "))
# print(f"Final Price = ${o_price-(o_price*(d_percent/100)):.2f}")

# cost_of_meal = eval(input("Enter the cost of your meal: "))
# tip_calulation = cost_of_meal * 0.20
# tax_calulation = cost_of_meal * 0.0825
# total_cost = cost_of_meal+tip_calulation+tax_calulation

# print(f"----- Meal Cost Break Down -----")
# print(f"{'Meal Cost:':<15} ${cost_of_meal:.2f}")
# print(f"{'Tip (20%):':<15} ${tip_calulation:.2f}")
# print(f"{'Tax  (8.25%):':<15} ${tax_calulation:.2f}")
# print(f"-------------------------------")
# print(f"{'Total Cost: ':<15} ${total_cost:.2f}")

names = ["Dimitri Nji", "Jordan Worrobah", "Leon Poulson"]

for i in range(len(names)):
    print(i+1,names[i])
