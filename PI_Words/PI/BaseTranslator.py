import math
import logging
from decimal import Decimal
from decimal import getcontext

'''
Converts an array where the ith digit corresponds to (1 / baseA)^(i + 1)
digits[i], return an array output of size precisionB where the ith digit
corresponds to (1 / baseB)^(i + 1) * output[i].

Stated in another way, digits is the fractional part of a number
expressed in baseA with the most significant digit first. The output is
the same number expressed in baseB with the most significant digit first.

To implement, logically, you're repeatedly multiplying the number by
baseB and chopping off the most significant digit at each iteration:

for (i < precisionB) {
  1. Keep a carry, initialize to 0.
  2. From RIGHT to LEFT
     a. x = multiply the ith digit by baseB and add the carry
     b. the new ith digit is x % baseA
     c. carry = x / baseA
  3. output[i] = carry

If digits[i] < 0 or digits[i] >= baseA for any i, return null
If baseA < 2, baseB < 2, or precisionB < 1, return null

@param digits The input array to translate. This array is not mutated.
@param baseA The base that the input array is expressed in.
@param baseB The base to translate into.
@param precisionB The number of digits of precision the output should
                  have.
@return An array of size precisionB expressing digits in baseB.

links used to solve:
http://baseconvert.com/
http://stackoverflow.com/questions/10972276/base-conversions-issue-with-fractions
http://math.stackexchange.com/questions/92631/convert-numbers-from-one-base-to-another-using-repeated-divisions?rq=1
http://math.stackexchange.com/questions/94677/convert-fractions-from-one-base-to-another-using-repeated-multiplications?rq=1
http://answers.yahoo.com/question/index?qid=20120129134806AAbfcW9
http://cs.stackexchange.com/questions/10318/the-math-behind-converting-from-any-base-to-any-base-without-going-through-base

TESTS: ../test/test_BaseTranslator.py
'''

logger = logging.getLogger(__name__)

def runMult(fraction, baseB=16):
    ''' ../test/test_BaseTranslator.py
    Runner for mult() to re-initialize the output list everytime it gets
    called. Using it in interactive mode was problematic, because the list
    wasn't empty anymore after the first use.
    '''
    output = []
    result = mult(fraction, baseB, output)
    logger.debug("runMult: %s" % result)
    return result

def mult(fraction, baseB, output):
    '''
    Recursive implementation of multplying a fraction, then cutting off the
    most significant number.
    '''
    global precision
    if precision > 0:
        prod = Decimal(fraction) * Decimal(baseB)
        int_prod = int(math.floor(prod))
        output.append(int_prod)
        radix_right = prod - int_prod
        if radix_right == 0.0:
            logger.debug("mult radix == 0 output: %s" % output)
            return output
        else:
            precision -= 1
            mult(radix_right, baseB, output)
            return output
    else:
        logger.debug("mult precision 0 output: %s" % str(output))
        return output

def toDec(digits, baseA):
    '''
    Convert a fraction of baseA to a decimal fraction.
    Input is a list of fractional digits.
    Example:
        0.56 = [5,6]
        toDec(56, 8)
        out: 0.71875
    '''
    # digit_list = list(str(digits))
    digit_list = digits
    dec_list = []
    # logger.debug(digit_list)
    for i, d in enumerate(digit_list):
        dec_d = Decimal(d)*Decimal(baseA)**-(i+1)
        dec_list.append(dec_d)
    # logger.debug(dec_list)
    output = Decimal(0)
    for i in dec_list:
        output += i
    logger.debug("toDec output: %s" % output)
    return output

def verifyInput(digits, baseA, baseB, precisionB):
    for d in digits:
        if d < 0:
            return 0
        if d >= baseA:
            return 0
    if baseA < 2 or baseB < 2:
        return 0
    if precisionB < 1:
        return 0
    return 1

def init(precisionB):
    global precision
    precision = precisionB
    getcontext().prec = precisionB

def convertBase(digits, baseA, baseB, precisionB):
    # Problem 2.b
    logger.debug("\nINPUT\n========\nbaseA: %s baseB: %s precisionB: %s " % (baseA, baseB, precisionB) )
    logger.debug("DIGITS\n " +str(digits) + "\n")
    if verifyInput(digits, baseA, baseB, precisionB):
        init(precisionB)
        dec = toDec(digits, baseA)
        logger.debug("converted to decimal (intermediate step): %s" % dec )
        rebased = runMult(dec, baseB)
        logger.info("final result of convertBase(): %s" % rebased )
        return rebased
    else:
        return 0

if __name__ == "__main__":
    '''
    Small self-test.
    '''
    # logging.basicConfig(level=logging.ERROR, filename="debug.log")
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    print(convertBase([5,6], 8, 10, 5))
    print(convertBase([5,6], 8, 16, 5))
