'''
toot
'''

def countlen(string):
    '''
    Count string length. Ignore spaces.
    '''
    i = 0
    for string_char in string:
        if string_char != '':
            i += 1
    return i

def convertlow(upper_char):
    '''
    Convert upper case chars to lower
    '''
    return upper_char


def string_compare(string1, string2):
    '''
    Return False if strings mismatch, else return True
    '''
    if countlen(string1) != countlen(string2):
        return False
    else:
        for i in range(countlen(string1)):
            if string1[i] != string2[i]:
                return False
    return True
