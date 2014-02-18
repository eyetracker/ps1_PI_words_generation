#!python3

import math
from collections import OrderedDict
import logging

class AlphabetGenerator():

    '''Given a numeric base, return a char[] that maps every digit that is
    representable in that base to a lower-case char.

    This method will try to weight each character of the alphabet
    proportional to their occurrence in words in a training set.

    This method should do the following to generate an alphabet:
      1. Count the occurrence of each character a-z in trainingData.
      2. Compute the probability of each character a-z by taking
         (occurrence / total_num_characters).
      3. The output generated in step (2) is a PDF of the characters in the
         training set. Convert this PDF into a CDF for each character.
      4. Multiply the CDF value of each character by the base we are
         converting into.
      5. For each index 0 <= i < base,
         output[i] = (the first character whose CDF * base is > i)

    A concrete example:
    	 0. Input = {"aaaaa..." (302 "a"s), "bbbbb..." (500 "b"s),
                  "ccccc..." (198 "c"s)}, base = 93
      1. Count(a) = 302, Count(b) = 500, Count(c) = 193
      2. Pr(a) = 302 / 1000 = .302, Pr(b) = 500 / 1000 = .5,
         Pr(c) = 198 / 1000 = .198
      3. CDF(a) = .302, CDF(b) = .802, CDF(c) = 1
      4. CDF(a) * base = 28.086, CDF(b) * base = 74.586, CDF(c) * base = 93
      5. Output = {"a", "a", ... (28 As, indexes 0-27),
                   "b", "b", ... (47 Bs, indexes 28-74),
                   "c", "c", ... (18 Cs, indexes 75-92)}

    The letters should occur in lexicographically ascending order in the
    returned array.
      - {"a", "b", "c", "c", "d"} is a valid output.
      - {"b", "c", "c", "d", "a"} is not.

    If base >= 0, the returned array should have length equal to the size of
    the base.

    If base < 0, return null.

    If a String of trainingData has any characters outside the range a-z,
    ignore those characters and continue.

    '''

    @staticmethod
    def generate_frequency_alphabet(base, trainingData):
        '''
        @Param base A numeric base to get an alphabet for.
        @Param trainingData The training data from which to generate frequency
                            counts. This array is not mutated.
        @RETURN A char[] that maps every digit of the base to a char that the
                digit should be translated into.
        '''

        logger = logging.getLogger(__name__)

        # Count occurence of chars in training data ###########################
        training_count = {}
        total_chars = 0
        for string in trainingData:
            for char in string:
                total_chars += 1
                if char in training_count:
                    training_count[char] += 1
                else:
                    training_count[char] = 1
        logger.debug(training_count)

        # Compute probability of each character ###############################
        pdf = {char: occurence/total_chars
                for char, occurence in training_count.items()}
        logger.debug("pdf" + str(pdf))

        def my_round(x):
            return int(x + math.copysign(0.5, x))

        # PDF * Base to determine intervals of each char in output alphabet ###
        pdf_indexes = OrderedDict([(char, math.floor(x*base))
            for char, x in pdf.items()])
        # logger.debug("pdf_indexes:" + str(pdf_indexes))

        # Generate PDF Alphabet ###############################################
        # alphabet = [key for key, value in pdf_indexes.items() for i in range(value)]
        # logger.debug(alphabet)
        # logger.debug(len(alphabet))
        # return alphabet

        # PROOF OF CONCEPT : CDF ##############################################
        # Compute cumulative density function #################################
        cdf = OrderedDict()
        counter = 0.0
        for i in sorted(pdf.items()):
            cdf[i[0]] = i[1] + counter
            counter += i[1]

        logger.debug(cdf)
        logger.debug(len(cdf))

        # CDF * Base to determine intervals of each char in output alphabet ###
        # cdf_indexes = OrderedDict([(char, int(round(x*base)))
        #     for char, x in cdf.items()])
        cdf_indexes = OrderedDict()
        for char, c_prob in cdf.items():
            cdf_indexes[char] = int(round(c_prob * base, 2))
        logger.debug("cdf indexes: " + str(cdf_indexes))

        cdf_ranges = OrderedDict()
        # 1st item, 2nd key: occurences
        # previous_occ = cdf_indexes.items()[0][1]
        previous_occ = 0
        for char, occ in cdf_indexes.items():
            cdf_ranges[char] = (previous_occ, occ)
            previous_occ = occ
        logger.debug("cdf ranges: " + str(cdf_ranges))

        # Generate Alphabet CDF style #########################################
        alphabet = []
        for i in range(base):
            for char, interval in cdf_ranges.items():
                if interval[0] <= i < interval[1]:
                    alphabet.append(char)
        logger.debug(alphabet)
        logger.debug(len(alphabet))
        return alphabet



if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)

    base = 21
    # trainingData = ['absdf', 'iosfdasodfh', 'ioufwoioiawehgahwgehoiawge']
    trainingData = ['abcd', 'abc', 'abeffg']
    # logger.debug(len(AlphabetGenerator.generate_frequency_alphabet(base, trainingData)))
    # logger.debug(AlphabetGenerator.generate_frequency_alphabet(base, trainingData))
    AlphabetGenerator.generate_frequency_alphabet(base, trainingData)

