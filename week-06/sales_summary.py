# associate_name, store_region, units_sold, price_per_unit = input("Please enter your name," \
#                                                                 "store region," \
#                                                                 "how many units sold,"
#                                                                 "price per unit: ").split(",")
# name = str(associate_name)
# region = str(store_region)
# units_sold = int(units_sold)
# price_per_unit = float(price_per_unit)

# def sales_summary(name, region, units, price):
#     total_revenue = units * price
#     performance_bonus = total_revenue * 0.10

#     print(f"{name} has earned ${total_revenue} and gained a bouns of ${performance_bonus}")



# sales_summary(name,region,units_sold,price_per_unit)
import random
fruits = [1,2,3,4,5,6,7,8,9,10]
print(random.shuffle(fruits))