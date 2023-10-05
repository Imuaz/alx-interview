#!/usr/bin/python3
"""
boxes unlock module
"""


def canUnlockAll(boxes):
    """method that checks if all boxes can be opened"""
    num_boxes = len(boxes)
    unlocked = [False] * num_boxes
    unlocked[0] = True  # Start with the first box unlocked
    keys = [0]  # Initialize a list of keys with the first box keys

    while keys:
        box_id = keys.pop()
        for key in boxes[box_id]:
            if not unlocked[key]:
                unlocked[key] = True
                keys.append(key)

    return all(unlocked)
