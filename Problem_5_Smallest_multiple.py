"""
Problem 5 Smallest multiple

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""


def is_divisible(n):
    for i in range(1, 21):
        if n % i != 0:
            return False
    return True

num = 2520
while not is_divisible(num):
    num += 2520

print(num)

