#!/usr/bin/python3
"""Lockboxes Algorithms"""


def checkKeys(boxes, keys, pair):
    """aux funtion to check values of keys"""
    new_pair = []
    check = False

    for i in pair:
        if not keys[i]:
            keys[i] = True
            new_pair += boxes[i]
            check = True
    
    res = {
        "pair": new_pair,
        "check": check
    }

    return res


def canUnlockAll(boxes):
    """Principal funtion"""
    keys = {}

    for i in range(len(boxes)):
        keys[i] = False 

    check = True
    pair = boxes[0]
    keys[0] = True

    while check:
        temp = checkKeys(boxes, keys, pair)
        pair = temp.get("pair")
        check = temp.get("check")

    for key, value in keys.items():
        if not value:
            return False

    return True
