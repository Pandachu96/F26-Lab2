# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Zebang Yang
# Date: 9/23/2026
# Purpose: Create a variable, check its type and print the variable.
# Usage: ./lab2a.py

# TO DO 1: Follow the instructions given in README.md file

x = input()

print(type(x))

x = int(x)

if x >= 6:
    print('x is greater or equal to 6!')
    
if x >= 4 and x < 12:
    print('x is >= 4 and < 12')