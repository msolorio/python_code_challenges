import math

def get_litres(hours):
    if not isinstance(hours, int) and not isinstance(hours, float):
        raise TypeError('parameter must be a number')

    return math.floor(hours * .5)
