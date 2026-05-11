# Name: Leon Poulson
# Date: 5/8/26
# Instructor: Deodat
# Calulate Tile Placement

length = eval(input("How long is your room: "))
width = eval(input("How wide is your room: "))

tiles = length + width
extra_tiles = tiles * 0.10
total_tiles =  tiles + extra_tiles
boxes_needed = total_tiles/12

print(f"You would need {total_tiles} tiles and {boxes_needed} tile boxes")