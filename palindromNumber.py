"""
Given an integer x, return true if x is palindrome integer.
"""

def isPalindrom(x:int) -> bool:
    if (x < 0 or (x %10 == 0 and x != 0)):
        return False
    rev = 0
    i = x
    while x > rev:
        rev = rev * 10 + i %10
        i = i//10
    return rev == x or rev == x/10


print(isPalindrom(11011))
