#!/usr/bin/python3
'''Method that determines if a given data set represents
a valid UTF-8 encoding.
'''

def validUTF8(data):
    """Checks if a list of integers are valid UTF-8 codepoints.
    See <https://datatracker.ietf.org/doc/html/rfc3629#page-4>
    """
    def get_bytes(num_bytes):
        """Returns a list of the next `num_bytes` bytes from `data`.
        """
        if i + num_bytes > n:
            return []
        return data[i+1 : i+num_bytes]

    i = 0
    n = len(data)
    while i < n:
        byte = data[i]
        num_bytes = 0
        if byte <= 0x7f:
            num_bytes = 1
        elif byte <= 0xdf:
            num_bytes = 2
        elif byte <= 0xef:
            num_bytes = 3
        elif byte <= 0xf7:
            num_bytes = 4
        else:
            return False
        bytes_list = get_bytes(num_bytes)
        if len(bytes_list) != num_bytes:
            return False
        for b in bytes_list:
            if not (0x80 <= b <= 0xbf):
                return False
        i += num_bytes
    return True

