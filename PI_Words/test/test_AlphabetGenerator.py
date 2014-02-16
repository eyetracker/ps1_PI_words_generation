
def generateFrequencyAlphabetTest():
    # Expect in the training data that Pr(a) = 2/5, Pr(b) = 2/5,
    # Pr(c) = 1/5.
    trainingData = ["aa", "bbc"]
    # In the output for base 10, they should be in the same proportion.
    expectedOutput = ['a', 'a', 'a', 'a',
                                'b', 'b', 'b', 'b',
                                'c', 'c']
    # assert expectedOutput == AlphabetGenerator.generateFrequencyAlphabet(
                    # 10, trainingData))
