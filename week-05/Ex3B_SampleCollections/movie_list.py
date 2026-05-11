# Name: Leon Poulson
# Date: 5/10/26
# Instructor: Deodat
# Manipulating lists

movies = ["Rio", "Up", "Lion King", "Ponyo"]

print(f"The list movies includes my top {len(movies)} favorite movies")
print(movies)

print(sorted(movies))
print(movies)

movies.sort()
print(movies)

movies.append("Mission Impossible")
print(f"The list movies now includes my top {len(movies)} favorite movies")
print(movies)