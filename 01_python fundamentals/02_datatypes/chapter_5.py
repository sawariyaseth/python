import sys
from fractions import Fraction
from decimal import Decimal

ideal_temp = 95.48
current_temp = 95.49

print(f"Ideal temp { ideal_temp }")
print(f"Current temp { current_temp }")
print(f"Difference temp { ideal_temp - current_temp }")
print(sys.float_info)

# sys is a python module that provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter. It is always available.