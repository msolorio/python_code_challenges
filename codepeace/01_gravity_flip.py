## Write a function that given the first parameter of 'R' will sort the second parameter, an array from smallest to largest. Given a first parameter of 'L' will sort an array from larget to smallest.

## flip('R', [3, 2, 1, 2])     =>  [1, 2, 2, 3]
## flip('L', [1, 4, 5, 3, 5])  =>  [5, 5, 4, 3, 1]

def flip(direction, array):
    if not isinstance(array, list):
        raise TypeError('second parameter must be a list')

    if direction == 'R':
        return sorted(array)
    if direction == 'L':
        return sorted(array, reverse=True)
    
    raise TypeError('first parameter must be "L" or "R"')

