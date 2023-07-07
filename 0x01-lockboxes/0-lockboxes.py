#!/usr/bin/python3
"""
New function to unock boxex
"""


def canUnlockAll(boxes):
    '''
    You have n number of locked boxes in front of you.
    Each box is numbered sequentially from 0 to n - 1
    and each box may contain keys to the other boxes.
    Write a method that determines if all the boxes can be opened.
    '''

    list_keys = [0]
    for i in list_keys:
        for j in boxes[i]:
            if j < len(boxes) and j not in list_keys:
                list_keys.append(j)
        if len(list_keys) == len(boxes):
            return True
    return False
