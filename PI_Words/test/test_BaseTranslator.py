#!/usr/bin/python3
from PI_Words.PI import BaseTranslator

ABORT = 0

def test_BasicBoundaries():
    cb = BaseTranslator.convertBase
    #Beware of bullshit: 0.-11 
    #Beware of bullshit: 0.1-1 
    assert cb([-1,1], 16, 10, 2) == ABORT
    assert cb([1,-1], 16, 10, 2) == ABORT

def test_RedundantBases():
    cb = BaseTranslator.convertBase
    assert cb([0,0], 1, 10, 2) == ABORT # baseA < 2
    assert cb([9,5], 10, 1, 2) == ABORT # baseB < 2
    assert cb([9,5], 10, 16, 0) == ABORT # precisionB < 1

def test_CorrectBase():
    cb = BaseTranslator.convertBase
    # 9 in base-8
    # 8 in base-8
    # 15 in base 10
    assert cb([9,1], 8, 2, 2) == ABORT
    assert cb([8,1], 8, 2, 2) == ABORT
    assert cb([15,1], 10, 2, 2) == ABORT

def test_mult():
    m = BaseTranslator.mult
    BaseTranslator.init(2)
    assert m(0.71875, 8, []) == [5,6]

def test_runMult():
    rm = BaseTranslator.runMult
    BaseTranslator.init(2)
    assert rm(0.71875, 8) == [5,6]

def test_basicBaseTranslator():
    cb = BaseTranslator.convertBase
    # Expect that .01 in base-2 is .25 in base-10
    # (0 * 1/2^1 + 1 * 1/2^2 = .25)
    feed = [0, 1]
    expectedOutput = [2, 5]
    assert cb(feed, 2, 10, 2) == expectedOutput

    # (1 / baseA)^(i + 1) * digits[i]
    # (2 / 10)^(0+1) * 7 = 7/10
    # (1 / 10)^(1+1) * 5 = 5/100
    # (1 / baseB)^(i + 1) * output[i]
    feed = [7, 5]
    # 0 * x ^ 1 + 1 * x ^ 2 + 2 * x ^ 3
    expectedOutput = [6]
    assert cb(feed, 10, 8, 1) == expectedOutput

def test_Base8Translator():
    cb = BaseTranslator.convertBase
    feed = [5] # base 8
    expect= [6,2,5] # base 10
    assert cb(feed, 8, 10, 3) == expect

    feed = [0,6] # base 8 
    expect= [0,9,3,7,5] # base 10
    assert cb(feed, 8, 10, 5) == expect

    feed = [5,6] # base 8
    expect= [7,1,8,7,5] # base 10
    assert cb(feed, 8, 10, 5) == expect

    feed = [7] # base 8
    expect= [8,7,5] # base 10
    assert cb(feed, 8, 10, 3) == expect

    feed = [7,5] # base 10 to 8 = 0.6
    expect= [6] # base 8
    assert cb(feed, 10, 8, 1) == expect

    # irrational number
    feed = [7] # base 10
    expect= [5,4,6,3,1,4] # base 8
    assert cb(feed, 10, 8, 6) == expect

def test_Base16Translator():
    cb = BaseTranslator.convertBase
    feed = [15] # base 16 to 10 = 0.9375 according to http://baseconvert.com/
    expect= [9,3,7,5] # base 10
    assert cb(feed, 16, 10, 4) == expect

    feed = [10, 10] # base 16 to 10 = 0.6640625
    expect= [6,6,4,0,6,2,5] # base 10
    assert cb(feed, 16, 10, 7) == expect

    # Hat rounding errors! Fix: More precision, cutting off the list
    feed = [7,5] # base 10 to 16 = 0.C according to http://baseconvert.com/
    expect= [12] # base 16
    assert cb(feed, 10, 16, 2) == expect

    feed = [4] # base 16 to 10 = 0.25 according to http://baseconvert.com/
    expect= [2,5] # base 10
    assert cb(feed, 16, 10, 2) == expect

def test_BaseTranslatePI():
    cb = BaseTranslator.convertBase
    # expectedOutput = [2,4,3,15,6,10,8,8,8,5]

    feed = [1,4,1,5 ,9,2 ,6,5,3,5] # base 10 to 16
    expect= [2,4,3,15,6,10,8,8,2,2,14,8] # base 10
    assert cb(feed, 10, 16, 12) == expect
    # Hat rounding errors! Fix: More precision, cutting off the list
    feed = [2,4,3,15,6,10,8,8,8,5] # base 16
    expect = [1,4,1,5 ,9,2 ,6,5,3,5,8,9,2,1] # base 10
    assert cb(feed, 16, 10, 15)[:14] == expect

# missing: base 26 translate 
# missing: translation of at least 43 digits. float numbers were used before,
# which capped the translation at 43 digits, which was resolved by switching to
# decimal.Decimal
