'''Method that determines if a given data set represents
a valid UTF-8 encoding.
'''

def is_valid_utf8(data):
    """Checks if a list of integers are valid UTF-8 codepoints.
    See <https://datatracker.ietf.org/doc/html/rfc3629#page-4>
    """
    n = len(data)
    i = 0

    while i < n:
        if data[i] < 0 or data[i] > 0x10FFFF:
            return False

        # 1-byte utf-8 character encoding
        if data[i] <= 0x7F:
            i += 1
        # 2-byte utf-8 character encoding
        elif 0xC2 <= data[i] <= 0xDF:
            if i + 1 >= n or not (0x80 <= data[i+1] <= 0xBF):
                return False
            i += 2
        # 3-byte utf-8 character encoding
        elif 0xE0 <= data[i] <= 0xEF:
            if i + 2 >= n or not (0x80 <= data[i+1] <= 0xBF and 0x80 <= data[i+2] <= 0xBF):
                return False
            i += 3
        # 4-byte utf-8 character encoding
        elif 0xF0 <= data[i] <= 0xF7:
            if i + 3 >= n or not (0x80 <= data[i+1] <= 0xBF and 0x80 <= data[i+2] <= 0xBF and 0x80 <= data[i+3] <= 0xBF):
                return False
            i += 4
        else:
            return False

    return True

