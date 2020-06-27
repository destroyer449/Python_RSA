# data transfer primitives
def os2ip(x):
    x_len = len(x)
    x = x[::-1]
    c = 0
    for i in range(x_len):
        c += x[i] * 256 ^ i
    return c


def i2osp(integer, size=4):
    return ''.join([chr((integer >> (8 * i)) & 0xFF) for i in reversed(range(size))])


# RSA primitives
def RSAEP(key, message):
    return pow(message, key[1], key[0])


def RSADP(key, cipher):
    return pow(cipher, key[1], key[0])


# signature primitives
def RSAPS1(key, m):
    return None
