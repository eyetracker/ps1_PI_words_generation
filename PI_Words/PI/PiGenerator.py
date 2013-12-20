#!/usr/bin/python3

import math

global DEBUG
DEBUG = False

if DEBUG:
    def debug(printstring):
        print(printstring)
else:
    def debug(doesntmatter):
        pass

class PiGenerator:
    ''' Returns precision hexadecimal digits of the fractional part of pi.
     Returns digits in most significant to least significant order.

     If precision < 0, return null.

     @param precision The number of digits after the decimal place to
                      retrieve.
     @return precision digits of pi in hexadecimal.
    '''

    @staticmethod
    def computePiInHex(precision):
        # TODO: Implement (Problem 1.d)
        return [0]


    # decorator for python 2! unbound method removed from python 3!
    @staticmethod
    def powerMod(a, b, m):
        ''' Computes a^b mod m

        If a < 0, b < 0, or m < 0, return -1.

        @param a
        @param b
        @param m
        @return a^b mod m
        TODO: Implement (Problem 1.b)'''

        if a | b | m < 0:
            return -1
        power = math.floor(a**b)
        carryover = power % m
        debug("== return powerMod: {0} ==".format(carryover));
        return carryover


    @staticmethod
    def piDigit(n):
        '''
        Computes the nth digit of Pi in base-16.

        If n < 0, return -1.

        @param n The digit of Pi to retrieve in base-16.
        @return The nth digit of Pi in base-16.

        NOTE: testing done in ../test/test_PiGeneratorTest.py|35|
        '''

        if n < 0:
            return -1
        n -= 1
        x = 4 * PiGenerator.piTerm(1, n) - 2 * PiGenerator.piTerm(4, n) - \
                   PiGenerator.piTerm(5, n) - PiGenerator.piTerm(6, n)
        x = x - math.floor(x)
        result = math.floor(x * 16)
        debug("-- return piDigit: {0} --".format(result));
        return result

    @staticmethod
    def piTerm(j, n):
        # Calculate the left sum
        debug("++ piTerm j, n: {0}, {1}".format(j, n))
        s = 0
        for k in range(0, n+1):
            r = 8 * k + j
            s += PiGenerator.powerMod(16, n-k, r) / r
            s = s - math.floor(s)
        # Calculate the right sum
        t = 0
        k = n+1
        # Keep iterating until t converges (stops changing)
        while 1:
            r = 8 * k + j
            newt = t + math.pow(16, n-k) / r
            if (t == newt):
                break
            else:
                t = newt
            k += 1
        result = s+t
        debug("++ return piTerm: {0} ++".format(result));
        return result

