#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
numstr = repr(number)
lastdigitstr = numstr[-1]
lastdigit = int(lastdigitstr)
if lastdigit > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, lastdigit))
elif lastdigit == 0:
    print("Last digit of {} is {} and is 0".format(number, lastdigit))
elif lastdigit < 6 and != 0:
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, lastdigit))
