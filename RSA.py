# RSA cryptographic security method
# TODO:
#   decryption method
#   class
#   protected attributes

import secrets
from oaep import Oaep
from functions import *
from primitives import *


def generate_prime(bits):
    while True:
        rand = secrets.randbits(bits)
        if is_prime(rand):
            return rand


def generate_keys(bits):
    p = generate_prime(bits // 2)
    q = generate_prime(bits // 2)
    n = p * q
    totient = lcm(p - 1, q - 1)
    e = 65537
    d = mod_inverse(e, totient)

    public_key = (n, e)
    private_key = (n, d)
    return public_key, private_key


def encode(message, key):
    o = Oaep(hashlib.sha3_512(), key)
    em = o.encrypt(message)
    m = os2ip(em)
    c = pow(m, key[1], key[0])
    c = i2osp(c, o.k)
    return c


def decode(cipher, key):
    c = os2ip(cipher)
    m = pow(c, key[1], key[0])
