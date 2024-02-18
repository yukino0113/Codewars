# https://www.codewars.com/kata/57fae964d80daa229d000126/train/python

def remove(s):
    if not s: return s
    return s[:-1] if s[-1] == '!' else s