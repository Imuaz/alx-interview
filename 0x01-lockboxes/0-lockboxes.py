#!/usr/bin/python3
"""
boxes unlock module
"""


def canUnlockAll(boxes):
    """method that checks if all boxes can be opened"""
    keys = [0]
    unlocked = []
    while True:
        if keys == unlocked:
            break
        for key in keys:
            if key not in unlocked:
                unlocked.append(key)
        for ibox in unlocked:
            current = boxes[ibox]
            for bx in current:
                if bx not in keys and bx < len(boxes):
                    keys.append(bx)
    return len(unlocked) == len(boxes)
