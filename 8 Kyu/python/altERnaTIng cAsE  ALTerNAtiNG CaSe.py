# https://www.codewars.com/kata/56efc695740d30f963000557/train/python

def to_alternating_case(string):
    return ''.join([x.lower() if x.isupper() else x.upper() for x in string])