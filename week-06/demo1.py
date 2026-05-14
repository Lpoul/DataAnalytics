# def even_or_odd(num):
#     if num%2 == 0:
#         return print(f"{num} is even")
#     else:
#         return print(f"{num} is odd")

# is_even_or_odd = eval(input("Please enter number to check if its even or odd: "))
# even_or_odd(is_even_or_odd)

def birthday_breakdown(birthday):
   
    DOB_splitter = str(birthday).split("/")
    month_num = int(DOB_splitter[0])
    day = int(DOB_splitter[1])
    year = int(DOB_splitter[2])
    if month_num == 1:
        month = "January"
    elif month_num == 2:
            month = "February"
    elif month_num == 3:
            month = "March"
    elif month_num == 4:
            month = "April"
    elif month_num == 5:
            month = "May"
    elif month_num == 6:
            month = "June"
    elif month_num == 7:
            month = "July"
    elif month_num == 8:
            month = "August"
    elif month_num == 9:
            month = "September"
    elif month_num == 10:
            month = "October"
    elif month_num == 11:
            month = "November"
    elif month_num == 12:
            month = "December"
    else:
            month = "Invalid month"   
    
    print(f"The month you were born was {month}.\n "
            f"The day you were born was {day}.\n"
            f"The year you were born was {year}.\n"
            f"You are {2026-year} years old.")

Date_of_Birth = str(input("Please enter in your birthday (MM/DD/YY): "))
birthday_breakdown(Date_of_Birth)