"""
Define a function that takes one integer argument and returns logical value true or false depending on if the integer is a prime.

Per Wikipedia, a prime number (or a prime) is a natural number greater than 1 that has no positive divisors other than 1 and itself.
"""
import math

def is_prime(num):
    if (num > 1):
        if (num == 2): return True
        if (num %2 == 0): return False
        for i in range(3, int(math.sqrt(num)) + 1, 2):
            if (num % i == 0):
                return False
        return True
    return False


print(is_prime(13))
