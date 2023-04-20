#!/usr/bin/python3

'''UTF-8 Validation'''


def validUTF8(data):
    '''method that determines if a given data
    set represents a valid UTF-8 encoding
    Return: True if data is a valid UTF-8 encoding,
    else return False'''

    leading_bytes = 0

    for byte in data:
        if leading_bytes == 0:
            if byte >> 7 == 0b0:
                continue
            elif byte >> 5 == 0b110:
                leading_bytes = 1
            elif byte >> 4 == 0b1110:
                leading_bytes = 2
            elif byte >> 3 == 0b11110:
                leading_bytes = 3
            else:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
            leading_bytes -= 1
    return leading_bytes == 0
