#!/usr/bin/python3

'''Rotate 2D Matrix'''


def rotate_2d_matrix(matrix):
    ''' rotate matrix 90 degrees clockwise'''

    copy = matrix[:]

    for i in range(len(matrix)):

        # extract the i column from the copy
        col_i = [row[i] for row in copy]

        # place it on the original matrix in reverse order
        matrix[i] = col_i[::-1]
