import sys


def get_size(num_bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if num_bytes < factor:
            return f"{num_bytes:.2f}{unit}{suffix}"
        num_bytes /= factor


def truncate(f, n):
    """Truncates/pads a float f to n decimal places without rounding"""
    s = '{}'.format(f)
    if 'e' in s or 'E' in s:
        return '{0:.{1}f}'.format(f, n)
    i, p, d = s.partition('.')
    return '.'.join([i, (d+'0'*n)[:n]])


def decimal_to_binary(n):
    return bin(n).replace("0b", "")


def decimal_to_hex(n):
    return hex(n).replace("0x", "")


def reverse_binary(n, bit_size=24):
    # return "0b" + str(n)[::-1]
    binary = bin(n)
    reverse_number = binary[-1:1:-1]
    reverse_number = reverse_number + (bit_size - len(reverse_number)) * '0'
    return int(reverse_number)


def get_bit(num, i):
    # print("{0:b}".format(num))
    binary_positional_value = (num & (1 << i))
    return binary_positional_value != 0
