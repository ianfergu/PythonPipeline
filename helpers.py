import random

"""
Helper functions that calculate the average of the list of numebers,
and then writes that value to test.txt
"""

def calculate():
    numbers = open("old.txt", "r")
    num = numbers.readline()

    count = 0
    total = 0

    while num != "":
        count += 1
        total += int(num[0:num.find('\n')]) + random.randint(0, 25)
        num = numbers.readline()

    return total / count


def write_test():
    average = calculate()

    test = open("test.txt", "r+")
    test.truncate()

    test.write(str(average))
