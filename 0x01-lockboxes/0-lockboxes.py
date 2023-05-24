#!/usr/bin/python3

'''Lockboxes - Each box is numbered sequentially from
0 to n - 1 and each box may contain keys to the other boxes'''


def canUnlockAll(boxes):
    '''determines if all the boxes can be opened.
    Return True if all boxes can be opened, else return False'''

    for key in range(1, len(boxes) - 1):
        ctr = False
        for idx in range(len(boxes)):
            ctr = (key in boxes[idx] and key != idx)
            if ctr:
                break
        if ctr is False:
            return ctr
    return True
