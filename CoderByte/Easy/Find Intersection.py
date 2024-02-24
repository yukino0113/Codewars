"""
https://coderbyte.com/information/Find%20Intersection
TEST CASE POINTS: 5
TIME PERIOD POINTS: 5
"""

def FindIntersection(strArr):

  a = strArr[0].split(', ')
  b = strArr[-1].split(', ')

  return [int(x) for x in a if x in b] or 'false'

# keep this function call here
print(FindIntersection(input()))