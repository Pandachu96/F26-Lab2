# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Zebang Yang
# Date: 9/23/2026
# Purpose: Learn how to use command line arguments.
# Usage: ./lab2f.py

# TO DO 1: Follow the instructions given in README.md file

import sys


if len(sys.argv) <= 1:
    print('The script requires at least 2 arguments.')

else:
    name = sys.argv[1]
    age = sys.argv[2]
    print('Hi {name}, you are {age} years old and the script received {length} arguments.'.format(
        name=name, age=age,length=len(sys.argv)-1))