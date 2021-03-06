from PI_Words.PI.DigitsToStringConverter import DigitsToStringConverter

convert = DigitsToStringConverter.convertDigitsToString

def test_invalidinput():
    # error: digits > base 
    assert 0 == convert([1,2], 1, ['b','a'])
    # digits < 0
    assert 0 == convert([-1], 1, ['b','a'])
    # length(alphabet) != base
    assert 0 == convert([1], 1, ['b','a'])
    assert 0 == convert([1], 2, ['a'])

def test_basicNumberSerializer():
    # Input is a 4 digit number, 0.123 represented in base 4
    inp = [0, 1, 2, 3]

    # Want to map 0 -> "d", 1 -> "c", 2 -> "b", 3 -> "a"
    alphabet = ['d', 'c', 'b', 'a']

    expectedOutput = "dcba";
    assert expectedOutput == convert(inp, 4, alphabet)

def test_bigNumberSerializer():
    inp = [8,12,22,14,17,10,8,13,6,5,8,13,4]
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    base = len(alphabet)
    expected = 'imworkingfine'
    assert expected == convert(inp, base, alphabet)

def test_OutputLength():
    inpSmall = [8,12,22,14,17,10,8,13,6,5,8,13,4]
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    base = len(alphabet)
    assert len(inpSmall) == len(convert(inpSmall,base, alphabet))
    inpLong = [8,12,22,14,17,10,8,13,6,5,8,13,4,8,12,22,14,17,10,8,13,6,5,8,13,
            4,8,12,22,14,17,10,8,13,6,5,8,13,4,8,12,22,14,17,10,8,13,6,5,8,13,
            4,8,12,22,14,17,10,8,13,6,5,8,13,4,8,12,22,14,17,10,8,13,6,5,8,13,
            4,8,12,22,14,17,10,8,13,6,5,8,13,4,8,12,22,14,17,10,8,13,6,5,8,13,
            4,8,12,22,14,17,10,8,13,6,5,8,13,4,8,12,22,14,17,10,8,13,6,5,8,13,
            4,8,12,22,14,17,10,8,13,6,5,8,13,4]
    assert len(inpLong) == len(convert(inpLong,base, alphabet))
