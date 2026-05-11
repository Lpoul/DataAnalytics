# Name: Leon Poulson
# Date: 5/11/26
# Instructor: Deodat
#Savings Calulator 


balance = eval(input("Enter your starting bank balance: "))
goal = eval(input("Enter your savings goal: "))
weekly_save = eval(input("Enter your weekly savings amount: "))

halfway = goal * 0.50
seventy_five = goal * 0.75

week = 1

while balance < goal:
    balance += weekly_save

    if balance >= seventy_five:
        treat = 5  # treat cost
        balance -= treat
        print(f"Week {week}: So close! After treating myself, my balance is up to {balance}.")
    
    elif balance >= halfway:
        print(f"Week {week}: Almost there! This week my balance is up to {balance}.")
    
    else:
        print(f"Week {week}: This week my balance increased to {balance}.")

    week += 1

print(f"\nGoal met! My current balance is {balance}.")