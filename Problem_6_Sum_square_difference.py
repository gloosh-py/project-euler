"""
Problem 6 - Sum square difference

The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is

3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""


sum_square = 0
square_sum = 0
sum_ = 0
j = 0

for i in range(101):

	sum_square += i**2

while j <= 100:

	sum_ += j
	j += 1

square_sum = sum_ ** 2

print(f"{square_sum - sum_square}")

print(sum_square)
print(square_sum)