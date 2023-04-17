#!/usr/bin/env python3

'''Pascal's triangle'''


def pascal_triangle(n):
    '''returns a list of lists of integers
    representing the Pascal’s triangle of "n"
    Returns an empty list if n <= 0'''

    if n <= 0:
        return []

    #initialize the triangle
    tri = [[1]]

    for count in range(1, n):
        #initialize the row
        row = [1]

        for count2 in range(1, count):
            #value to be appended to row
            value = tri[count - 1][count2 - 1] + tri[count - 1][count2]
            row.append(value)

        row.append(1)

        #append the row to the triangle
        tri.append(row)

    return tri
