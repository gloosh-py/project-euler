"""
Problem 4 Largest palindrome product

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""



def is_palindrome(x):
    return str(x) == str(x)[::-1]

largest_palindrome = 0
largest_factors = (0, 0)

for i in range(100, 1000):
    for j in range(100, 1000):
        product = i * j
        if is_palindrome(product) and product > largest_palindrome:
            largest_palindrome = product
            largest_factors = (i, j)

print(f"The largest palindrome is {largest_palindrome} and is a product of {largest_factors[0]} and {largest_factors[1]}")