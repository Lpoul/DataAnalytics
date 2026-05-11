name_1 = "PRIYA SHARMA"
name_2 = "bob NGUYEN"
name_3 = "LaTonya Williams"

salary_1 = "$82,500"
salary_2 = "$74,000"

lower_name_1 = name_1.lower()
lower_name_2 = name_2.lower()
lower_name_3 = name_3.lower()

print(f"lower_1: {lower_name_1} {type(lower_name_1)}")
print(f"lower_2: {lower_name_2} {type(lower_name_2)}")
print(f"lower_3: {lower_name_3} {type(lower_name_3)}")

title_name_1 = name_1.title()
title_name_2 = name_2.title()
title_name_3 = name_3.title()

print(f"title_1: {title_name_1} {type(title_name_1)}")
print(f"title_2: {title_name_2} {type(title_name_2)}")
print(f"title_3: {title_name_3} {type(title_name_3)}")

salary_1_no_dollar = salary_1.replace("$", "")
salary_2_no_dollar = salary_2.replace("$", "")
print(f"salary 1 with no dollar sign: {salary_1_no_dollar} {type(salary_1_no_dollar)}")
print(f"salary 2 with no dollar sign: {salary_2_no_dollar} {type(salary_2_no_dollar)}")
#You would have to convert them to floats in order to start performing math on them

salary_1_int = int(salary_1.replace("$", "").replace(",", ""))
print(f"salary 1 to int: {salary_1_int} {type(salary_1_int)}")