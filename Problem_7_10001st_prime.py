"""
Problem 7 10001st prime 

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def nth_prime(n):
    """Find the nth prime number."""
    count = 0
    num = 2
    while count < n:
        if is_prime(num):
            count += 1
        if count == n:
            return num
        num += 1


print(nth_prime(10001))
