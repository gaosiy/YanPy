"""
Functions for handling numbers
"""


def int2bin(n: int, n_bits: int = 0) -> str:
    """
    Convert decimal integer to binary

    :param int n: decimal integer
    :param int n_bits: set length for the output
    :return: binary number as a string
    :rtype: str
    :raise ValueError: If the nBits is not enough to store the input number
    """
    if n_bits == 0:
        n_bits = n.bit_length()
    elif n_bits < n.bit_length():
        raise ValueError('Number of bit is too small.')
    bin_str = ''.join([str((n >> y) & 1) for y in range(n_bits - 1, -1, -1)])
    return bin_str


def bin2int(n: str) -> int:
    """
    Convert binary to decimal integer

    :param str n: binary integer
    :return: decimal number
    :rtype: int
    """
    ret = int(n, 2)
    return ret


def bin2gray(bin_code: str) -> str:
    """
    Convert binary code to gray code

    :param str bin_code: binary code
    :return: gray code
    :rtype: str
    """
    gray_code = (bin2int(bin_code) >> 1) ^ bin2int(bin_code)
    return int2bin(gray_code, n_bits=len(bin_code))


def gray2bin(gray_code: str) -> str:
    """
    Convert gray code to binary code

    :param str gray_code: gray code
    :return: binary code
    :rtype: str
    """
    bin_code = [gray_code[0]]
    i = 1
    while i < len(gray_code):
        bin_code.append(str(int(bin_code[i - 1]) ^ int(gray_code[i])))
        i = i + 1
    return "".join(bin_code)


def int2gray(n: int, n_bits: int = 0) -> str:
    """
    Convert integer to gray code

    :param str n: a decimal integer
    :param int n_bits: set length for the output
    :return: gray code
    :rtype: str
    :raise ValueError: If the nBits is not enough to store the input number
    """
    gray_code = (n >> 1) ^ n
    return int2bin(gray_code, n_bits=n_bits)


def gray2int(gray_code: str) -> int:
    """
    Convert gray code to decimal integer

    :param str gray_code: gray code
    :return: decimal integer
    :rtype: int
    """
    bin_code = [gray_code[0]]
    i = 1
    while i < len(gray_code):
        bin_code.append(str(int(bin_code[i - 1]) ^ int(gray_code[i])))
        i = i + 1
    bin_code = "".join(bin_code)
    return bin2int(bin_code)


if __name__ == '__main__':
    print('1. int2bin:')
    print('int 7 equals to bin ' + str(int2bin(7, n_bits=4)))
    print('2. bin2int:')
    print('bin 0111 equals to int ' + str(bin2int('0111')))
    print('3. bin2gray:')
    print('bin 0111 equals to gray code ' + str(bin2gray('0111')))
    print('4. gray2bin:')
    print('gray code 0100 equals to bin ' + str(gray2bin('0100')))
    print('5. int2gray:')
    print('int 7 equals to gray code ' + str(int2gray(7, n_bits=4)))
    print('6. gray2int:')
    print('gray code 0100 equals to int ' + str(gray2int('0100')))
    print('Quick demo for number module:')
