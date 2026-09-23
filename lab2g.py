# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Zebang Yang
# Date: 9/23/2026
# Purpose: Learn how and practice using nested if, elif, and else statments..
# Usage: ./lab2g.py

# TO DO 1: Follow the instructions given in README.md file
# Initialize constant variables for the tax rates and rate limits.

income = int(input())
status = input()

# Tax calculation for single status:
if status.lower() == 'single':
    if income <= 32000:
        tax = 0.1 * income

    elif income > 32000:
        tax = 3200 + 0.25 * (income - 32000)

# Tax calculation for married status:
if status.lower() == 'married':
    if income <= 64000:
        tax = 0.1 * income

    elif income >64000:
        tax = 6400 + 0.25 * (income - 64000)

print(tax)