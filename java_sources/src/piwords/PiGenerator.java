package piwords;

import java.math.BigInteger;

public class PiGenerator {
    /* package piwords; */
    /**
     * Returns precision hexadecimal digits of the fractional part of pi.
     * Returns digits in most significant to least significant order.
     * 
     * If precision < 0, return null.
     * 
     * @param precision The number of digits after the decimal place to
     *                  retrieve.
     * @return precision digits of pi in hexadecimal.
     */
    public static int[] computePiInHex(int precision) {
        // TODO: Implement (Problem 1.d)
        //
        int[] PiInHex = new int[precision];
        for (int i = 0; i < precision; i++){
            PiInHex[i] = PiGenerator.piDigit(i);
        }
        return PiInHex;
    }

    /**
     * Computes a^b mod m
     * 
     * If a < 0, b < 0, or m < 0, return -1.
     * 
     * @param a
     * @param b
     * @param m
     * @return a^b mod m
     */
    /* public static int powerMod(int a, int b, int m) { */
    /*     // TODO: Implement (Problem 1.b) */
    /*     return -1; */
    /* } */

    /* From online compiler */
    /* http://www.compileonline.com/compile_java_online.php */

    /* public static void main(String []args){ */
    /*     System.out.println(); */

    /*     System.out.print(piDigit(0)); */
    /*     /* System.out.printf("%n NEW DIGIT %n"); */
    /*     System.out.print(" "); */
    /*     System.out.print(piDigit(1)); */
    /*     /* System.out.printf("%n NEW DIGIT %n"); */
    /*     System.out.print(" "); */
    /*     System.out.print(piDigit(2)); */
    /*     System.out.print(" "); */
    /*     System.out.print(piDigit(3)); */
    /*     System.out.print(" "); */
    /*     System.out.print(piDigit(4)); */
    /*     System.out.print(" "); */
    /*     System.out.println(); */
    /* } */

    public static double powerMod(int a, int b, int m) {
        /*''' Computes a^b mod m

          If a < 0, b < 0, or m < 0, return -1.

          @param a
          @param b
          @param m
          @return a^b mod m
    TODO: Implement (Problem 1.b)'''*/
        double carryover;
        double power;

        if (a < 0 | b < 0| m < 0) return -1;
        /* power = Math.pow(a, b); */
        /* carryover = power % m; */
        BigInteger a_big = BigInteger.valueOf(a);
        BigInteger b_big = BigInteger.valueOf(b);
        BigInteger m_big = BigInteger.valueOf(m);
        BigInteger result_big = a_big.modPow(b_big, m_big);
        int result = result_big.intValue();
        /* System.out.printf("== return powerMod: %f ==%n", carryover); */
        return result;
    }

    /**
     * Computes the nth digit of Pi in base-16.
     * 
     * If n < 0, return -1.
     * 
     * @param n The digit of Pi to retrieve in base-16.
     * @return The nth digit of Pi in base-16.
     */
    public static int piDigit(int n) {
        if (n < 0) return -1;

        n -= 1;
        double x = 4 * piTerm(1, n) - 2 * piTerm(4, n) -
            piTerm(5, n) - piTerm(6, n);
        x = x - Math.floor(x);
        int result = (int)(x * 16); 
        /* System.out.printf("-- return piDigit: %d --%n", result); */
        return result;
    }

    private static double piTerm(int j, int n) {
        // Calculate the left sum
        double s = 0;
        for (int k = 0; k <= n; ++k) {
            int r = 8 * k + j;
            s += powerMod(16, n-k, r) / (double) r;
            s = s - Math.floor(s);
        }

        // Calculate the right sum
        double t = 0;
        int k = n+1;
        // Keep iterating until t converges (stops changing)
        while (true) {
            int r = 8 * k + j;
            double newt = t + Math.pow(16, n-k) / r;
            if (t == newt) {
                break;
            } else {
                t = newt;
            }
            ++k;
        }
        double result = s+t;
        /* System.out.printf("++ return piTerm: %f ++%n", result); */
        return result;
    }
}
