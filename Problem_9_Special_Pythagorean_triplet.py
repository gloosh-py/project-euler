"""
Problem 9 Special Pythagorean triplet 


A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 3ˆ2 + 4ˆ2 = 9 + 16 = 25 = 5ˆ2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


for a in range(1, 400):
  for b in range(1, 400):
    c = (1000 - a) - b
    if a < b < c:
      if a**2 + b**2 == c**2:
        print(a * b * c)