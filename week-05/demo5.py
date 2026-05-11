# # Working with Sets: U.S. States

# states = {"New York", "California", "Texas", "Florida", "Illinois"}

# print(f"Total number of states: {len(states)}")

# print(f"Is Texas in the set? {'Texas' in states}")


# print(f"States in alphabetical order: {sorted(states)}")

# longest_length = 0
# for state in states:
#     if len(state) > longest_length:
#         longest_length = len(state)

# print(f"Length of the longest state name: {longest_length}")


# states.add("Georgia")
# print(f"Set after adding Georgia: {states}")


# states.discard("Florida")
# print(f"Set after removing Florida: {states}")
num = 0
count = 0
num = eval(input("Please enter a number: "))
while num>=0:
    num = eval(input("Please enter a number: "))
    count+=1
    num = num+num
    if num<0:
        count-=1

print(f"This is how many times the loop ran: {count}")