# -*- coding: utf-8 -*-
from __future__ import absolute_import
from abc import ABCMeta, abstractmethod
from random import SystemRandom
from fcrypter.base import custom_exceptions as cryexc
from Crypto.Random import get_random_bytes


class Cryptor(object):
    __metaclass__ = ABCMeta

    """
    Abstract class for defining file encryption interface
    """

    def __init__(self, supported_sizes):
        """
        Constructor

        :param supported_sizes: supported key sizes for encryption/decryption
        :type supported_sizes: tuple
        """
        self.supported_sizes = supported_sizes

    def generate_random_password(self, size=None, chars=None):
        """
        Random password generator
        If size not specified, chooses randomly from the supported sizes
        If chars are specified, generates password for those chars
        Else generates random size bytes

        :param size: password size
        :type size: int
        :param chars: chars to choose password from
        :type chars: iterable
        :return: random password
        :rtype: bytes
        """
        rand = SystemRandom()
        if not size:
            size = self.supported_sizes[rand.randint(
                0, len(self.supported_sizes)-1)]
        if not chars:
            return get_random_bytes(size)

        return bytes("".join((rand.choice(chars) for _ in range(size))))

    def verify_supported_key_size(self, key):
        """
        Verifies key size is supported

        :param key: key to be used for encryption
        """
        if self.supported_sizes and len(key) not in self.supported_sizes:
            raise cryexc.WrongKeySizeError(
                "Supported key sizes are {sizes}".format(
                    sizes=", ".join((str(x) for x in self.supported_sizes))))

    @abstractmethod
    def encrypt_file(self, key, f_path, encr_fpath):
        """
        File encryption base method

        Needs a key, a file path to encrypt and a resulting file path for the
        encrypted file to be saved

        :param key: a key to use for the file encryption
        :param f_path: absolute path for the file to be encrypted
        :param encr_fpath: absolute path for the encrypted file to be saved
        """
        pass

    @abstractmethod
    def decrypt_file(self, key, encr_fpath, decr_fpath):
        """
        File decryption base method

        Needs a key, a file path to decrypt and a resulting file path for the
        decrypted file to be saved

        :param key: a key to use for the file decryption
        :param encr_fpath: absolute path for the encrypted file
        :param decr_fpath: absolute path for the decrypted file to be saved
        """
        pass
