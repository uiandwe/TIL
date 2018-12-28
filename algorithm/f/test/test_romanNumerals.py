import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import RomanNumerals


def test_solve():
    assert 'I' == RomanNumerals.roman(1)
    assert 'II' == RomanNumerals.roman(2)
    assert 'III' == RomanNumerals.roman(3)
    assert 'IV' == RomanNumerals.roman(4)
    assert 'V' == RomanNumerals.roman(5)
    assert 'VIII' == RomanNumerals.roman(8)
    assert 'IX' == RomanNumerals.roman(9)
    assert 'X' == RomanNumerals.roman(10)
    assert 'XL' == RomanNumerals.roman(40)
    assert 'XLII' == RomanNumerals.roman(42)
    assert 'XXXIX' == RomanNumerals.roman(39)
    assert 'CCXLVI' == RomanNumerals.roman(246)
    assert 'CCVII' == RomanNumerals.roman(207)
    assert 'MLXVI' == RomanNumerals.roman(1066)
    assert 'MDCCLXXVI' == RomanNumerals.roman(1776)
    assert 'MCMLIV' == RomanNumerals.roman(1954)
