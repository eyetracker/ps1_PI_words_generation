from PI_Words.PI.AlphabetGenerator import AlphabetGenerator as AG
# import logger

# gfa = AG.generate_frequency_alphabet

def test_correct_input():
    pass

def test_generateFrequencyAlphabetTest():
    # Expect in the training data that Pr(a) = 2/5, Pr(b) = 2/5,
    # Pr(c) = 1/5.
    trainingData = ["aa", "bbc"]
    # In the output for base 10, they should be in the same proportion.
    expectedOutput = ['a', 'a', 'a', 'a',
                                'b', 'b', 'b', 'b',
                                'c', 'c']
    returned = AG.generate_frequency_alphabet( 10, trainingData)
    assert len(expectedOutput) == len(returned)
    assert expectedOutput == returned

def test_fullAlphabet():
    # Pr(\w) = 1/26.
    trainingData = ["abcdefghijklm", "nopqrstuvwxyz"]
    expectedOutput = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
            'y', 'z']

    assert expectedOutput == AG.generate_frequency_alphabet( 26, trainingData)

def test_base_100_alphabet():
    base = 93
    trainingData = ["a"*302, "b"*500, "c"*198]
    expect = ["a"]*28 + ["b"]*46 + ["c"]*19
    returned = AG.generate_frequency_alphabet(base, trainingData)
    print(returned[27:29])
    print(returned[73:76])
    assert AG.generate_frequency_alphabet(base, trainingData) == expect


