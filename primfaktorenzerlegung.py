def isprime(num):
    for n in range(2,int(num**1/2)+1):
        if num%n==0:
            return False
    return True

def divisors(integer):
    if (isprime(integer)): return f"${integer} is prime"
    solution = []
    divisor = 2
    while (divisor <= integer):
        if (integer/divisor == int(integer/divisor)):
            integer /= divisor
            solution.append(divisor)
        else:
            print(divisor)
            divisor += 1
    return solution


print(divisors(12))
