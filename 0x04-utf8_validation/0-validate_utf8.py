#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """
    Method that determines if a given data set represents
    a valid UTF-8 encoding.
    """

    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Mask to check if the most significant bit is set
    mask1 = 1 << 7

    # Mask to check if the second most significant bit is set
    mask2 = 1 << 6

    for byte in data:
        # If this is the start of a new character
        if num_bytes == 0:
            # Count the number of bytes in this UTF-8 character
            if byte & mask1 == 0:
                num_bytes = 1
            elif byte & (mask1 >> 1) == 0b11000000:
                num_bytes = 2
            elif byte & (mask1 >> 2) == 0b11100000:
                num_bytes = 3
            elif byte & (mask1 >> 3) == 0b11110000:
                num_bytes = 4
            else:
                return False
            # Decrement num_bytes to handle the current byte
            num_bytes -= 1
        else:
            # Check if the byte is a continuation byte
            if not (byte & mask1 and not (byte & mask2)):
                return False
            # Decrement num_bytes to indicate a continuation byte
            num_bytes -= 1

    return num_bytes == 0
