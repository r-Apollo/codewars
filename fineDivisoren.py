"""
Create a function named divisors/Divisors that takes an integer n > 1 and returns an array with all of the integer's 
divisors(except for 1 and the number itself), 
from smallest to largest. If the number is prime return the string '(integer) is prime' 
"""

"""
def divisors(integer):
    solution = []
    divisor = 2
    while (divisor < integer):
        if(integer/divisor == int(integer/divisor)):
            solution.append(divisor)
        divisor += 1
    if(len(solution) == 0): return f"{integer} is prime"
    return solution
"""

def divisors(integer):
    d = [i for i in range(2, integer) if integer%i == 0]
    if (len(d) == 0): return f"{integer} is prime"
    return d

print(divisors(25))

