# Name: Leon Poulson
# Date: 5/11/26
# Instructor: Deodat
# Calulating Pay


pay_rate = eval(input("Enter pay rate: "))
hours_worked = eval(input("Enter hours worked: "))

if hours_worked > 40:
    regular_hours = 40
    overtime_hours = hours_worked - 40
    gross_pay = (regular_hours * pay_rate) + (overtime_hours * pay_rate * 1.5)
else:
    gross_pay = hours_worked * pay_rate

print(f"Gross pay: ${gross_pay:.2f}")