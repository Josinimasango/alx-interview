#!/usr/bin/python3
'''a method that determines if all the boxes can be opened'''


def canUnlockAll(boxes):
    '''checking if all boxes can open sucessfully or not'''
    num_boxes = len(boxes)
    keys = set(boxes[0])
    opened_boxes = [0]

    for box in opened_boxes:
        for key in boxes[box]:
            if key != 0 and key < num_boxes and key not in opened_boxes:
                opened_boxes.append(key)
                keys.update(boxes[key])

    for i in range(1, num_boxes):
        if i not in opened_boxes:
            return False
    return True
