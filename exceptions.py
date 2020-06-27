# exceptions for use in the cryptography package
# TODO:
#   write RSA errors


class OaepError(Exception):
    def __init__(self, msg):
        super().__init__("OAEP Error Type: "+msg)


class OaepEncryptionError(OaepError):
    def __init__(self, msg):
        super().__init__("Encryption Error: "+msg)


class OaepDecryptionError(OaepError):
    def __init__(self, msg):
        super().__init__("Decryption Error: " + msg)


if __name__ == "__main__":
    raise OaepDecryptionError("decryption error")
