# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Zebang Yang
# Date: 9/23/2026
# Purpose: use for loop.
# Usage: ./lab2k.py

# TO DO 1: 
#Follow the instructions given in the README.md file.

# Use a for loop to iterate over the list
#for fruit in fruits:
#    print(fruit)

#for loop is commonly used with range functions. Here's another example using the range function to print numbers from 0  to 5.
sum = 0
for num in range(1, 101):
    if num % 2 == 0:
        sum += num

print(sum)