# https://www.codewars.com/kata/515e271a311df0350d00000f/train/python

def square_sum(numbers):
    for i in range(len(numbers)):
        numbers[i] = numbers[i]**2
    return sum(numbers)