# exceptions for use in the cryptography package
# TODO:
#   write RSA errors


class OaepError(Exception):
    pass


class OaepEncryptionError(OaepError):
    pass


class OaepDecryptionError(OaepError):
    pass
