# -*- coding: utf-8 -*-
"""

Running in Tim Industries

Created on Sun Nov 27 01:05:00 2022
in Tims II Lab

@author: Stark
"""

class NotWrittenError(Exception):
    def __init__(self, message = None):
        if message is not None:
            message = str(message)
            self.message = message
        else:
            self.message = "Something"
        self.message += " is not written yet"
        super().__init__(self.message)


class NoDefinitionError(Exception):
    def __init__(self, message = None):
        if message is not None:
            message = str(message)
            self.message = message
        else:
            self.message = "Something"
        self.message += " is not define"
        super().__init__(self.message)


class NoAccessError(Exception):
    def __init__(self, message = None):
        self.message = "You dont have access to change "
        if message is not None:
            message = str(message)
            self.message += message
        else:
            self.message += "it"
        super().__init__(self.message)


class NotMatchingError(Exception):
    def __init__(self, message = None):
        if message is not None:
            message = str(message)
            self.message = message
        else:
            self.message = "Something"
        self.message += " are not matching to each other"
        super().__init__(self.message)