#https://www.codewars.com/kata/5875b200d520904a04000003/train/python


def enough(cap, on, wait):
    return on+wait-cap if on+wait>cap else 0