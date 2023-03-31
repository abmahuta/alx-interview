#!/usr/bin/python3
'''A program that checks if all lockedboxes can be unlocked.
'''


def canUnlockAll(boxes):
    '''Checks if all the boxes in a list of boxes containing the keys
    (indices) to other boxes can be unlocked given that the first
    box is unlocked.
    '''
    n = len(boxes)
    seen_boxes = [0]
    unseen_boxes = boxes[0][:]
    while unseen_boxes:
        boxIdx = unseen_boxes.pop()
        if not boxIdx or boxIdx >= n or boxIdx < 0:
            continue
        if boxIdx not in seen_boxes:
            unseen_boxes.extend(boxes[boxIdx])
            seen_boxes.append(boxIdx)
    return n == len(seen_boxes)
