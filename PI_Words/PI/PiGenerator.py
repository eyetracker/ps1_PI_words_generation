import math

class PiGenerator():
    ''' Returns precision hexadecimal digits of the fractional part of pi.
     Returns digits in most significant to least significant order.

     If precision < 0, return null.

     @param precision The number of digits after the decimal place to
                      retrieve.
     @return precision digits of pi in hexadecimal.
    '''

    def computePiInHex(precision):
        # TODO: Implement (Problem 1.d)
        return [0]


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
        power = a**b
        carryover = power % m
        return carryover

    # Computes the nth digit of Pi in base-16.
    #
    # If n < 0, return -1.
    #
    # @param n The digit of Pi to retrieve in base-16.
    # @return The nth digit of Pi in base-16.

    def piDigit(n):
        if n < 0:
            return -1
        n -= 1
        x = 4 * piTerm(1, n) - 2 * piTerm(4, n) - \
                   piTerm(5, n) - piTerm(6, n)
        x = x - Math.floor(x)
        return x * 16

    def piTerm(j, n):
        # Calculate the left sum
        s = 0
        for k in range(0, n):
            r = 8 * k + j
            s += powerMod(16, n-k, r) / r
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
        return s+t

