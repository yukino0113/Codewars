# https://www.codewars.com/kata/65ba420888906c1f86e1e680/train/python

def collinearity(x1, y1, x2, y2):
    if x1 == y1 == 0 or x2 == y2 == 0:
        return True
    v1 = x1/y1 if y1 else 'inf'
    v2 = x2/y2 if y2 else 'inf'
    return v1==v2
