"""Classes for Exceptions"""


class Error(Exception):
    """Base class for other exceptions"""
    pass


class InputListTooLong(Error):
    def __init__(self, inp_list, message="The Input List is longer then 1"):
        self.inp_list = inp_list
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.inp_list} -> {self.message}'


class MonthlyListNotRightLength(Error):
    def __init__(self, inp_list, message="The List is not the size of 12"):
        self.inp_list = inp_list
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.inp_list} -> {self.message}'