#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """
    Method that determines if a given data set represents
    a valid UTF-8 encoding.

    Shifting right say, by 5 positions effectively isolates the three most
    significant bits (MSBs) of the byte.

    Then checks if the three most significant bits of the byte match
    the pattern 110, indicating that the byte is the start of a 2-byte
    UTF-8 character
    """

    num_bytes = 0

    for byte in data:
        if num_bytes == 0:
            if byte >> 5 == 0b110:
                num_bytes = 1
            elif byte >> 4 == 0b1110:
                num_bytes = 2
            elif byte >> 3 == 0b11110:
                num_bytes = 3
            elif byte >> 7 == 0b1:
                # If the most significant bit (MSB) is set, indicating an
                # invalid UTF-8 character, return False
                return False
        else:
            # If num_bytes is not 0, check if the byte is a continuation byte
            if byte >> 6 != 0b10:
                return False
            # Decrement num_bytes to indicate processing of a continuation byte
            num_bytes -= 1

    return num_bytes == 0
