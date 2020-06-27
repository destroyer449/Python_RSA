import hashlib
import math
import random
from primitives import *


def mgf1(message, length, hash_used=hashlib.sha3_512):
    counter = 0
    output = ''
    while len(output) < length:
        c = i2osp(counter, 4)
        output += hash_used(message + c).digest()
        counter += 1
        return output[:length]


def mod_inverse(a, m):
    m0 = m
    y = 0
    x = 1
    while a > 1:
        # q is quotient
        q = a // m
        t = m
        m = a % m
        a = t
        t = y
        # Update x and y
        y = x - q * y
        x = t
    # Make x positive
    if x < 0:
        x = x + m0
    return x


def lcm(x, y):
    """This function takes two
    integers and returns the L.C.M."""
    least_common_multiple = (x * y) // math.gcd(x, y)
    return least_common_multiple


def is_prime(n):
    """
    Miller-Rabin primality test.

    A return value of False means n is certainly not prime. A return value of
    True means n is very likely a prime.
    """
    # Miller-Rabin test for prime
    s = 0
    d = n - 1
    while d % 2 == 0:
        d >>= 1
        s += 1
    assert (2 ** s * d == n - 1)

    def trial_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2 ** i * d, n) == n - 1:
                return False
        return True

    for i in range(8):  # number of trials
        a = random.randrange(2, n)
        if trial_composite(a):
            return False

    return True
