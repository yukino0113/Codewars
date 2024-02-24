#https://www.codewars.com/kata/57f222ce69e09c3630000212/train/python

def well(x):
    if x.count('good') > 2:return 'I smell a series!'
    elif x.count('good') == 0:return 'Fail!'
    else:return 'Publish!'