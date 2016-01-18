#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Python Veralite™
   Okpe Pessu <opessu@zgreatone.net>

   Module holding exceptions
"""


class VeraliteException(Exception):
    """
    Base exception used by this module.
    pass
    """
    pass


class VeraliteConnectionError(VeraliteException):
    def __init__(self, code, message):
        self.code = code
        VeraliteException.__init__(self, "-%s- %s" % (code, message))


class InvalidDeviceError(VeraliteException):
    def __init__(self, message):
        VeraliteException.__init__(self, message)

class InvalidSceneError(VeraliteException):
    def __init__(self, message):
        VeraliteException.__init__(self, message)
