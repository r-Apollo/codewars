"""
Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.

The binary number returned should be a string.

Examples:(Input1, Input2 --> Output (explanation)))
"""


def add_binary(a,b):
    return format((a+b), "b")

print(add_binary(1, 1))
