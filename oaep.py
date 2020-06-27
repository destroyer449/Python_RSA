# OAEP padding system for use in RSA encryption decryption
# TODO:
#   decrypt method
#   protected attributes
#   test security

import secrets
from exceptions import *
from functions import *
from primitives import *


class Oaep:
    def __init__(self, h, key):
        self.key = key
        self.hash_used = h
        self.h_len = self.hash_used.digest_size
        self.k = len(oct(key[0])[2:])
        self.hash_used.update(b"")
        self.lhash = self.hash_used.digest()

    def encrypt(self, message):
        if type(message) is not bytes:
            raise OaepEncryptionError("Message must be Bytes")
        m_len = len(message)
        if m_len > self.k - self.h_len*2 - 2:
            raise OaepEncryptionError("Message Too Long")
        ps = b""
        for i in range(self.k - m_len - self.h_len*2 - 2):
            ps += b"10"
        db = self.lhash + ps + b"1" + message
        seed = b""
        for i in range(self.h_len):
            seed += bytearray(secrets.choice(range(256)))
        db_mask = mgf1(seed, self.k - self.h_len - 1)
        masked_db = db ^ db_mask
        seed_mask = mgf1(masked_db, self.h_len)
        masked_seed = seed ^ seed_mask
        em = b"0" + masked_seed + masked_db
        return em
