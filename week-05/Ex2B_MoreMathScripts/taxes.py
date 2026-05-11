# Name: Leon Poulson
# Date: 5/8/26
# Instructor: Deodat
# Calulate Federal Taxes

money_made = eval(input("How much money do you make a month: "))
taxes = money_made * 0.23
money_yearly = money_made*12
print(f"This is how much money you would have made in a year ${money_yearly:.2f} this is how much you are paying in taxes per month ${taxes:.2f}")