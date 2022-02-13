"""
You will be given a number and you will need to return it as a string in Expanded Form. For example:
12 => 10 + 2
312 => 300 + 10 + 2
70304 => 70000 + 300 + 4
"""

def expanded_form(num):
    arr = [int(e) * 10 ** i for i, e in enumerate(str(num)[::-1])][::-1]
    return " + ".join(str(i) for i in arr if i != 0)

print(expanded_form(70304))
