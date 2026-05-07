# Name: Leon Poulson
# Date: 5/7/26
# Instructor: Deodat
# Calulate the rule of 72

savings_num = 300
interest_rate = 0.05
rule_of_seven_two = 72/(interest_rate * 100)
savings_num_doubled = 600

print(f"Your current savings is {savings_num}.")
print(f"At a {interest_rate}% interest rate, your savings account will be worth ${savings_num_doubled:.2f} in {rule_of_seven_two:.1f} years")
