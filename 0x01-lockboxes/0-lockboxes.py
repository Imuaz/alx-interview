#!/usr/bin/python3
"""
boxes unlock module
"""
from collections import deque


def canUnlockAll(boxes):
    """method that checks if all boxes can be opened"""
    num_boxes = len(boxes)
    visited = [False] * num_boxes
    visited[0] = True  # Start with the first box visited
    queue = deque([0])  # Initialize a queue with the first box

    while queue:
        box_id = queue.popleft()
        for key in boxes[box_id]:
            if not visited[key]:
                visited[key] = True
                queue.append(key)
    return all(visited)
