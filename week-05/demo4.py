

student = ("Alice", 20, "Data Analytics", 3.5, True)

print(student)
print(f"Name    : {student[0]}")
print(f"Age     : {student[1]}")
print(f"Major   : {student[2]}")
print(f"GPA     : {student[3]}")
print(f"Active  : {student[4]}")
print(f"Length  : {len(student)}")


# count(x)
t = (1, 2, 2, 3, 2)
print(t.count(2))

print(t.index(2))


states = ("New York", "California", "Texas", "Florida", "Illinois")


print(f"Total number of states: {len(states)}")


print(f"First state: {states[0]}")
print(f"Last state: {states[-1]}")


print(f"Is Texas in the tuple? {'Texas' in states}")


print(f"States in alphabetical order: {sorted(states)}")


longest_state = 0

for state in states:
    if len(state) > longest_state:
        longest_state = len(state)

print(f"Longest state name length: {longest_state}")




