'''
Integration tests for the functions in src/simple.py.

Each test below combines the output of one function with the input of
another function in order to check that they work together correctly.
'''

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.simple import (  # noqa: E402
    evens,
    lengths,
    small_words,
    squares,
    threes,
)


def test_lengths_of_small_words():
    words = small_words('this is a simple test case')
    assert lengths(words) == [4, 2, 1, 4, 4]


def test_lengths_of_evens_as_strings():
    strings = list(map(str, evens(20)))
    assert lengths(strings) == [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2]


def test_threes_that_are_even():
    both = sorted(set(threes(40)) & set(evens(40)))
    assert both == [30, 32, 34, 36, 38]


def test_threes_are_bounded_by_evens():
    assert max(threes(50)) <= max(evens(50))


def test_small_words_of_squares():
    text = ' '.join(map(str, squares(12)))
    assert small_words(text) == [
        '1', '4', '9', '16', '25', '36',
        '49', '64', '81', '100', '121', '144',
        ]


def test_lengths_of_squares_as_strings():
    strings = list(map(str, squares(10)))
    assert lengths(strings) == [1, 1, 1, 2, 2, 2, 2, 2, 2, 3]


def test_small_words_of_evens_and_threes():
    text = ' '.join(map(str, evens(6) + threes(15)))
    assert small_words(text) == ['0', '2', '4', '6', '3', '13']


def test_empty_results_compose():
    assert lengths(small_words('')) == []
    assert lengths(list(map(str, evens(-1)))) == []
    assert lengths(list(map(str, threes(2)))) == []
