"""
The function parts_sums (or its variants in other languages) will take as parameter a list ls and return 
a list of the sums of its parts as defined above.

ls = [0, 1, 3, 6, 10]
ls = [1, 3, 6, 10]
ls = [3, 6, 10]
ls = [6, 10]
ls = [10]
ls = []

he corresponding sums are (put together in a list): [20, 20, 19, 16, 10, 0]
"""

"""
def parts_sums(ls):
    ls.append(0)
    return[sum(ls[i[0]:]) for i in enumerate(ls)]
"""
#My solutions runtime is way too high the function below is taken from the solutions
def parts_sums(ls):
    result = [sum(ls)]
    for item in ls:
        result.append(result[-1]-item)
    return result


print(parts_sums([744125, 935, 407, 454, 430, 90, 144, 6710213, 889, 810, 2579358]))
