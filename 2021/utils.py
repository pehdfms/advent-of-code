""" Utility functions for Advent of Code 2018 """
import re
from functools import reduce
import operator

class defaultlist(list):
    def __init__(self, fx):
        self._fx = fx

    def __setitem__(self, index, value):
        while len(self) <= index:
            self.append(self._fx())
        list.__setitem__(self, index, value)

    def __getitem__(self, index):
        """Allows self.dlist[0] style access before value is initialized."""
        while len(self) <= index:
            self.append(self._fx())
        return list.__getitem__(self, index)

def lmap(func, *iterables):
    """ Returns list of mapped items to func """
    return list(map(func, *iterables))

def lfilter(cond, *iterables):
    """ Returns list of items filtered by cond """
    return list(filter(cond, *iterables))

def fsum(func, iterable):
    """ Returns sum of func(x) for x in iterable """
    return sum(func(x) for x in iterable)

def string_diff(s1, s2):
    """ Count of diff characters in s1, s2 """
    diff = 0
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            diff += 1
    return diff

def get_ints(s):
    """ Returns list of all ints in line """
    return lmap(int, re.findall(r"-?\d+", s))

def get_words(s):
    """ Returns list of words in line """
    return re.findall(r"[a-zA-Z]+", s)

def get_data(day):
    """ Returns list of lines in input_file """
    with open(f'day{day}.txt', 'r') as input_file:
        return [data.strip() for data in input_file]

def invert(matrix):
    res = [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]
    return res

def adjacents(coord, sub = []):
    if not coord:
        yield sub
    else:
        yield from [idx for j in range(coord[0] - 1, coord[0] + 2) for idx in adjacents(coord[1:], sub + [j]) if idx != coord]

def identity(obj):
    return obj

def product(iterable):
    return reduce(operator.mul, iterable, 1)
