# -*- coding: utf-8 -*-
from collections import namedtuple
import aes


supported_ciphers = namedtuple("ciphers", ("name", "callclass"))


def get_aes_supported_modes():
    """
    Returns a named tuple with supported AES cipher modes and their class
    name callback
    """
    return supported_ciphers(name="AES-EAX", callclass=aes.AESCryptorEAX)


def get_supported_ciphers():
    """
    Returns a list of named tuples with supported cipher name and callback
    class name
    :rtype: tuple of namedtuples
    """
    return sum((tuple([x]) for x in (get_aes_supported_modes(),)), tuple())
