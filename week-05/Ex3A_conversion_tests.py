# Description: This script tests various numeric
# conversion techniques
# Author: Sam Q. Newprogrammer

a = "101.1 "
b = '55'
c = "402 Stevens"
d = 'Number 5 '

a_float = float(a) 
int_float_a = int(float(a))
# int_a = int(a)
stripped_a = a.strip()


b_int = int(b)
b_float = float(b)
# int_c = int(c)        # Value Error 
# float_c = float(c)    # Value Error 
int_c_fixed = int(c[0:3])

# int_d = int(d)        # Value Error
# float_d = float(d)    # Value Error
int_d_fixed = int(d[-2])
stripped_d = d.strip()


print(f"a: '{a}'", type(a))
print(f"float_a:", a_float, type(a_float))
print(f"int_from_float_a:", int_float_a, type(int_float_a))

print(f"b: {b} {type(b)}")
print(f"int_b: {b_int} {type(b_int)}")
print(f"float_b:{b_int} {type(b_int)}")

print(f"c: {c} {type(c)}")
print(f"c_num: {int_c_fixed} {type(int_c_fixed)}")

print(f"d: {d} {type(d)}")
print(f"d_num: {int_d_fixed} {type(int_d_fixed)}")
