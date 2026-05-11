# Name: Leon Poulson
# Date: 5/11/26
# Instructor: Deodat
# Calulating Taxes

pay_rate = eval(input("Enter your hourly pay rate: "))
hours_worked = eval(input("Enter hours worked this week: "))
filing_status = input("Enter filing status ('single' or 'joint'): ").lower()

if hours_worked > 40:
    regular_hours = 40
    overtime_hours = hours_worked - 40
    gross_pay = (regular_hours * pay_rate) + (overtime_hours * pay_rate * 1.5)
else:
    gross_pay = hours_worked * pay_rate

annual_gross = gross_pay * 52

if filing_status == "single":
    if annual_gross < 12000:
        tax_rate = 0.05
    elif annual_gross < 25000:
        tax_rate = 0.10
    elif annual_gross < 75000:
        tax_rate = 0.15
    else:
        tax_rate = 0.20

elif filing_status == "joint":
    if annual_gross < 12000:
        tax_rate = 0.00
    elif annual_gross < 25000:
        tax_rate = 0.06
    elif annual_gross < 75000:
        tax_rate = 0.11
    else:
        tax_rate = 0.20

else:
    print("Invalid filing status entered.")
    tax_rate = 0

weekly_tax = gross_pay * tax_rate
net_pay = gross_pay - weekly_tax

print(f"\nYou worked {hours_worked} hours this period.")
print(f"Because you earn ${pay_rate} per hour, your gross weekly pay is ${gross_pay:.2f}")
print(f"Your filing status is {filing_status}")
print(f"Your estimated annual gross income is ${annual_gross:.2f}")
print(f"Your tax withholding for the week is ${weekly_tax:.2f}")
print(f"Your net pay is ${net_pay:.2f}")