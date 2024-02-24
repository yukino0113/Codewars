"""
https://coderbyte.com/information/Codeland%20Username%20Validation
TEST CASE POINTS: 5
TIME PERIOD POINTS: 5
"""



def CodelandUsernameValidation(strParam):
    if not 4 <= len(strParam) <= 25:
        return 'false'

    if not strParam[0].isalpha():
        return 'false'

    if strParam[-1] == '_':
        return 'false'

    for i in strParam:
        if not (i.isdigit() or i.isalpha() or i == '_'):
            return 'false'

    return 'true'


# keep this function call here
print(CodelandUsernameValidation(input()))