# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Zebang Yang
# Date: 9/23/2026
# Purpose: Learn how to use command line arguments.
# Usage: ./lab2e.py

# TO DO 1: Follow the instructions given in README.md file

import sys


'''
print(sys.version) # prints the version of the python currently in use.
print(sys.platform) # prints the name of operating system.
print(sys.argv) # prints the list of all arguments given at the command line when running our python script from terminal.
print(len(sys.argv)) # tells us the number of command line arguments the user provides from terminal.

- Run your script using the command `python ./lab2d.py`
- Observe the output. How many arguments were passed to python this time?  Only one, which is your script name. You will see the path to your script file in the output of  print(sys.argv).
- Add the following lines to your script.
  

print(sys.argv[0]) # prints the first argument, it is always the name of script.
print(sys.argv[1]) # prints the second argument .
print(sys.argv[2]) # prints the third argument.
'''
# print(len(sys.argv)) # tells us the number of command line arguments the user provides from terminal.

if len(sys.argv) == 1:
    print('This script requires exactly two arguments. No arguments were provided!')

elif len(sys.argv) == 3:
    print('Hello user, good job, your provided two arguments!')

elif len(sys.argv) == 4:
    print('This script requires exactly two arguments. You provided three arguments.')
