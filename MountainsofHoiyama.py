"""
In the planet named Hoiyama, scientists are trying to find the weights of the mountains.
They managed to find the weights of some mountains.
But calculating them manually takes a really long time.
That's why they hired you to develop an algorithm and easily calculate the weights of the mountains.
Your function has only one parameter which is the width of the mountain and you need to return the weight of that mountain.
The widths of the mountains are only odd numbers.
They gave you some information about calculating the weight of a mountain.
Examine the information given below and develop a solution accordingly.
"""

def mountains_of_hoiyama(width):
    height = int((width+1)/2)
    value = width
    solution = 0
    for i in range(height, 0, -1):
        if (value == width):
            solution += sum(value-i for i in range(height))
            value -= 2
        else:
            solution += 2*(sum(value-i for i in range(height)))
            value -= 2
    return solution

mountains_of_hoiyama(9)
