"""A first look at the random module: print a random whole number from 0 to 9."""

import random

# random.random() gives a float in [0, 1); scaling by 10 and truncating with
# int() turns it into a whole number between 0 and 9.
a = int(random.random() * 10)

print(a)
