# https://www.codewars.com/kata/65128732b5aff40032a3d8f0/train/python

def neutralise(s1, s2):
    return ''.join([x if x==s2[n] else '0' for n, x in enumerate(s1)])
