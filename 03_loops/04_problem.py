# Problem: Reverse a string using a loop.

str = "Tisha"
reverse_str =""

for char in str:
    reverse_str=char+reverse_str
print(reverse_str)


#  visual flow

# Original String:  T  i  s  h  a
#                   ↓  ↓  ↓  ↓  ↓

# Start:
# reverse_str = ""

# 1st iteration:
# char = "T"
# reverse_str = "T" + ""
#              = "T"

# 2nd iteration:
# char = "i"
# reverse_str = "i" + "T"
#              = "iT"

# 3rd iteration:
# char = "s"
# reverse_str = "s" + "iT"
#              = "siT"

# 4th iteration:
# char = "h"
# reverse_str = "h" + "siT"
#              = "hsiT"

# 5th iteration:
# char = "a"
# reverse_str = "a" + "hsiT"
#              = "ahsiT"