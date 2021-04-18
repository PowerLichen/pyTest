# Calculate two value
"""
  Project: Calculate two value
  Author: Minsu Choe
  Date of last update: Mar. 12, 2021
"""

# define variable
var_a=int(input("input a = "))
var_b=int(input("input b = "))


#define calculated variable
add_val = var_a + var_b
sub_val = var_a - var_b
mul_val = var_a * var_b
div_val = var_a / var_b
int_div_val = var_a // var_b
mod_val = var_a % var_b

#print divider
print("================")


# print answer
print("a + b =", add_val)
print("a - b =", sub_val)
print("a * b =", mul_val)
print("a / b =", div_val)
print("a // b =", int_div_val)
print("a % b =", mod_val)

