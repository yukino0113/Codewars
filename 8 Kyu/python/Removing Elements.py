# https://www.codewars.com/kata/5769b3802ae6f8e4890009d2/train/python

def remove_every_other(my_list):
    return [x for n, x in enumerate(my_list) if not n%2]