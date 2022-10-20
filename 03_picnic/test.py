#!/usr/bin/env python3
"""tests for picnic.py"""

import os
from subprocess import getoutput

prg = './picnic.py'


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['', '-h', '--help']:
        out = getoutput(f'{prg} {flag}')
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_usage_delimiter_and_nocoma():
    """usage when flag for delimiter and nocoma used"""

    out = getoutput(f'{prg} -d: -n chips')
    assert out.lower().startswith('error :')

        
# --------------------------------------------------
def test_usage_delimiter_string():
    """usage when flag for delimiter is not char but string"""

    out = getoutput(f'{prg} -d::: chips')
    assert out.lower().startswith('error :')


# --------------------------------------------------
def test_one():
    """one item"""

    out = getoutput(f'{prg} chips')
    assert out.strip() == 'You are bringing chips.'


# --------------------------------------------------
def test_one_nocoma():
    """one item without coma"""

    out = getoutput(f'{prg} -n chips')
    assert out.strip() == 'You are bringing chips.'


# --------------------------------------------------
def test_two():
    """two items"""

    out = getoutput(f'{prg} soda "french fries"')
    assert out.strip() == 'You are bringing soda and french fries.'


# --------------------------------------------------
def test_two_nocoma():
    """two items without coma"""

    out = getoutput(f'{prg} -n soda "french fries"')
    assert out.strip() == 'You are bringing soda and french fries.'


# --------------------------------------------------
def test_two_delimiter():
    """two items with delimiter"""

    out = getoutput(f'{prg} -d: soda "french fries"')
    assert out.strip() == 'You are bringing soda:french fries.'


# --------------------------------------------------
def test_more_than_two():
    """more than two items"""

    arg = '"potato chips" coleslaw cupcakes "French silk pie"'
    out = getoutput(f'{prg} {arg}')
    expected = ('You are bringing potato chips, coleslaw, '
                'cupcakes, and French silk pie.')
    assert out.strip() == expected


# --------------------------------------------------
def test_more_than_two_nocoma():
    """more than two items without coma"""

    arg = '"potato chips" coleslaw cupcakes "French silk pie"'
    out = getoutput(f'{prg} -n {arg}')
    expected = ('You are bringing potato chips coleslaw '
                'cupcakes and French silk pie.')
    assert out.strip() == expected


# --------------------------------------------------
def test_more_than_two_delimiter():
    """more than two items with delimiter"""

    arg = '"potato chips" coleslaw cupcakes "French silk pie"'
    out = getoutput(f'{prg} -d: {arg}')
    expected = ('You are bringing potato chips:coleslaw:'
                'cupcakes:French silk pie.')
    assert out.strip() == expected


# --------------------------------------------------
def test_two_sorted():
    """two items sorted output"""

    out = getoutput(f'{prg} -s soda candy')
    assert out.strip() == 'You are bringing candy and soda.'


# --------------------------------------------------
def test_two_sorted_nocoma():
    """two items sorted output with no coma"""

    out = getoutput(f'{prg} -n -s soda candy')
    assert out.strip() == 'You are bringing candy and soda.'


# --------------------------------------------------
def test_two_sorted_delimiter():
    """two items sorted output with delimiter"""

    out = getoutput(f'{prg} -d: -s soda candy')
    assert out.strip() == 'You are bringing candy:soda.'


# --------------------------------------------------
def test_more_than_two_sorted():
    """more than two items sorted output"""

    arg = 'bananas apples dates cherries'
    out = getoutput(f'{prg} {arg} --sorted')
    expected = ('You are bringing apples, bananas, cherries, and dates.')
    assert out.strip() == expected

    
# --------------------------------------------------
def test_more_than_two_sorted_nocoma():
    """more than two items sorted output with no coma"""

    arg = 'bananas apples dates cherries'
    out = getoutput(f'{prg} -n {arg} --sorted')
    expected = ('You are bringing apples bananas cherries and dates.')
    assert out.strip() == expected


# --------------------------------------------------
def test_more_than_two_sorted_delimiter():
    """more than two items sorted output with delimiter"""

    arg = 'bananas apples dates cherries'
    out = getoutput(f'{prg} -d : {arg} --sorted')
    expected = ('You are bringing apples:bananas:cherries:dates.')
    assert out.strip() == expected

