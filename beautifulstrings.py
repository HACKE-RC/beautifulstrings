import platform
import logging

if not platform.python_implementation() == "CPython":
        logging.error("Unsupported Python variant!")

import forbiddenfruit
import codecs
import binascii

def _unhex(string):
        try:
                return codecs.decode(string, 'hex')
        except binascii.Error:
                return codecs.decode(string.replace("0x", ""), 'hex')

def _bytes(string):
        return codecs.encode(string, 'latin1')

def _str(string):
        return string.decode('latin1')

def _hex(string):
        return codecs.encode(string.bytes(), 'hex')

def _nop(string):
        return string

def _ascii(string):
        return "".join([str(ord(char)) for char in string])

def _ascii_list(string):
        return list(map(ord, string))


forbiddenfruit.curse(bytes, "str", _str)
forbiddenfruit.curse(str, "bytes", _bytes)
forbiddenfruit.curse(str, "str", _nop)
forbiddenfruit.curse(bytes, "bytes", _nop)
forbiddenfruit.curse(str, "ascii", _ascii)
forbiddenfruit.curse(str, "ascii_list", _ascii_list)
forbiddenfruit.curse(bytes, "unhex", _unhex)
forbiddenfruit.curse(str, "unhex", _unhex)
forbiddenfruit.curse(str, "hex", _hex)