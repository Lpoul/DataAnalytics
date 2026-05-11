# Name: Leon Poulson
# Date: 5/11/26
# Instructor: Deodat
#Looping though lists


items = ["tacos", "ramen", "jerk chicken", "injera", "pierogi"]

for index, item in enumerate(items, start=1):
    if index == 1:
        print(f"{index}. {item} <- top pick!")
    else:
        print(f"{index}. {item}")