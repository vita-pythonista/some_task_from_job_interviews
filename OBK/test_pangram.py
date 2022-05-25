# -*- coding: utf-8 -*-

import pytest

from pangram import is_pangram


class TestPangram:

    def test_empty_string(self):
        assert not is_pangram('')

    def test_valid_pangram(self):
        assert is_pangram('the quick brown fox jumps over the lazy dog')

    def test_missing_x(self):
        assert not is_pangram('a quick movement of the enemy will jeopardize five gunboats')

    def test_mixedcase_and_punctuation(self):
        assert is_pangram('"Five quacking Zephyrs jolt my wax bed."')

    def test_unchecked_german_umlaute(self):
        assert is_pangram('Victor jagt zwölf Boxkämpfer quer über den großen Sylter Deich.')
