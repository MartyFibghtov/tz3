import math
from typing import List


def read_numbers(filename: str):

    try:
        with open(filename, 'r') as file:
            for line in file.readlines():
                for num in map(float, line.split()):
                    yield num

    except FileNotFoundError:
        raise ValueError("File does not exist")


def get_min(filename: str) -> float:
    res = None

    for num in read_numbers(filename):
        if res is None:
            res = num
        elif num < res:
            res = num
    return res


def get_max(filename: str) -> float:
    res = None

    for num in read_numbers(filename):
        if res is None:
            res = num
        elif num > res:
            res = num
    return res


def get_sum(filename: str):
    res = 0
    for num in read_numbers(filename):
        res += num
    return res


def get_prod(filename: str):
    res = 1
    for num in read_numbers(filename):
        try:
            res *= num
        except OverflowError:
            return None
        if math.isinf(res):
            return None
    return res

