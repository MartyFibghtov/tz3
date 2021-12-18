import pytest

import random as rd
from typing import List
from math import prod
from math import isinf

from main import read_numbers, get_min, get_max, get_sum, get_prod


def gen_rand_numbers(amount: int = None) -> List[int]:
    res = []

    if amount is None:
        amount = range(rd.randint(1, 10000))
    for i in amount:
        res.append(rd.randint(-10 * (10 ** 10), 10 * (10 ** 10)))

    return res


def gen_rand_del() -> str:
    res = ""
    space_del = " \n\t"
    for i in range(rd.randint(1, 100)):
        res += rd.choice(space_del)

    return res


def write_numbers(numbers: List[int], filename: str, rand_del=False):
    with open(filename, 'w') as f:
        for n in numbers:
            delim = '\n'
            if rand_del:
                delim = gen_rand_del()
            f.write("{}{}".format(str(n), delim))


def test_basic_file():
    filename = "basic"
    f_exp = [1, 2, 3.2, 4.5, 4.5]
    write_numbers(f_exp, filename)
    f_res = list(read_numbers(filename))
    assert len(f_exp) == len(f_res)
    for i in range(len(f_exp)):
        assert f_res[i], f_exp[i]


def test_no_file():
    filename = 'file_does_not_exist'
    with pytest.raises(ValueError):
        list(read_numbers(filename))


def test_rand_delim():
    filename = "rand_delim"
    f_exp = [1, 2, 3.2, 4.5, 4.5]
    write_numbers(f_exp, filename, rand_del=True)
    f_res = list(read_numbers(filename))
    assert len(f_exp) == len(f_res)
    for i in range(len(f_exp)):
        assert f_res[i] == f_exp[i]


def test_empty_file():
    filename = "empty_file"
    with open(filename, 'w') as file:
        pass

    f_res = list(read_numbers(filename))
    assert 0 == len(f_res)


def test_basic():
    filename = 'basic_min_max'
    numbers = [1, 2, -3.2, 4.5, 4.5]
    write_numbers(numbers, filename)

    # Expected values
    min_exp = min(numbers)
    max_exp = max(numbers)
    sum_exp = sum(numbers)
    prod_exp = prod(numbers)

    # Got values
    min_res = get_min(filename)
    max_res = get_max(filename)
    sum_res = get_sum(filename)
    prod_res = get_prod(filename)

    assert min_exp == min_res
    assert max_exp == max_res
    assert sum_exp == sum_res
    assert prod_exp == prod_res


def test_big_sum_prod(self):
    filename = 'big_prod_sum'
    numbers = [10000 for i in range(10000)]
    write_numbers(numbers, filename)
    prod_res = get_prod(filename)
    self.assertIsNone(prod_res)


def test_equal():
    filename = 'equal_nums'
    numbers = [5 for i in range(10)]
    write_numbers(numbers, filename)

    # Expected values
    min_exp = min(numbers)
    max_exp = max(numbers)
    sum_exp = sum(numbers)
    prod_exp = prod(numbers)

    # Got values
    min_res = get_min(filename)
    max_res = get_max(filename)
    sum_res = get_sum(filename)
    prod_res = get_prod(filename)

    assert min_exp == min_res
    assert max_exp == max_res
    assert sum_exp == sum_res
    assert prod_exp == prod_res


def test_nothing():
    filename = 'no_numbers'
    numbers = []
    write_numbers(numbers, filename)

    # Expected values
    sum_exp = sum(numbers)
    prod_exp = prod(numbers)

    # Got values
    sum_res = get_sum(filename)
    prod_res = get_prod(filename)
    assert sum_exp == sum_res
    assert prod_exp == prod_res
