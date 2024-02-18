# https://www.codewars.com/kata/577bd026df78c19bca0002c0/train/python

def correct(s):
    d = {'5':'S', '0':'O', '1':'I'}
    return ''.join([d[x] if x in d else x for x in s])