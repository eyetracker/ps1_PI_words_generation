#!ipython3

pi_f = 0.1415926
pi = []
for i in range(10):
    pi.append(str(pi_f * i*16)[0])

print(pi)


def convertBase(digits, baseA, baseB, precisionB):
    return output

#0.56 b8 to b10
#(1/base) ^ (i+1) *x


to10('56')

test = list(str(56))
test

27 9 3
    33


0.3212 * 3
4*1.5
0.3212* 4/6

3*3**-1
2*3**-2
1*3**-3
2*3**-4

# 2*10 
# 16+4 = 0x14
# 0x16 = 16 + 6 = 22
# 0x22 / 0xa = 2 r 2 
16*2+2
#34/10 = 3 r 4
30%16
#14
# 1*16 + 14
# 14 = 0xE
# 1*16+14 = 0x1E

0x3/0xA
# 3/10 = 0.3
# 3/10 = 0 r 3

# Solange durch die neue basis teilen, bis ein unteilbarer rest übrig ist.
# Diese Teilung bringt ganze Zahlen bei der Division hervor.
# Diese ist die nächste Zahl, welche widerum geteilt wird.

# to base-3
0x2BA

16**3
#schema
4096 256 16 1
#hier nur 256 und weniger von interesse
2*256 + 0xB*16 + 0xA*1
11*16
512+ 10+ 176 = 698
0x2BA = 2*256 + B*16 + A*1 = 698

698/3
0x2BA%0x03
0x2B8/0x03
232/16
16*14+8
0xe8%3
0xe7/3
77%3
75/3
25%3
24/3
8%3
6/3
2%3
0/3

# mod's above order:
# 212122
# reversed, true order:
# 221212

# base-8 to base-10
0o72

0o72%10
0o62/10
0o5%10
0o0/10


0o0.56
0o12
56%12
48/12
4%12
0/12

0.5/0.12

5*8**-1
6*8**-2

7*8**1
2*8**0

0o56 to 0x...

0.625/16
= 0.0390625

import math
def runMult(fraction, baseB=16):
    output = []
    return mult(fraction, baseB, output)

def mult(fraction, baseB, output):
    '''
    only base-16 now!
    '''
    prod = fraction * float(baseB)
    print("prod: ",prod)
    int_prod = int(math.floor(prod))
    if int_prod >= 1:
        output.append(int_prod)
    radix_right = prod - int_prod
    print("radix_right: ", radix_right)
    if radix_right == 0.0:
        print("output: ", output)
        return output
    else:
        mult(radix_right, baseB, output)

(mult(0.5))
(mult(0.56))
runMult(0.71875, 8)
runMult(0.1415926535)

p = math.pi-3
p
(((((((((((((((((((((((((p*16)-2)*16)-4)*16)-3)*16)-15)*16)-6)*16)-10)*16)-8)*16)-8)*16)-8)*16)-5)*16)-10)*16)-3)*16)

0.56
d = 5*8**-1 + 6*8**-2
((((d*16)-11)*16)-8)
11 = b
8 = 8

0o0.56 == 0x0.b8

#b16 to b26
0x0.243f6a8885a3
0.3HIGBEBOHK


def toDec(digits, baseA):
    '''
    takes fractional part as list
    Example:
        0.56 = [5,6]
        toDec(56, 8)
        out: 0.71875
    '''
    # digit_list = list(str(digits))
    digit_list = digits
    dec_list = []
    # print(digit_list)
    for i, d in enumerate(digit_list):
        dec_d = float(d)*baseA**-(i+1)
        dec_list.append(dec_d)
    # print(dec_list)
    output = 0.0
    for i in dec_list:
        output += i
    return output

toDec([5,6], 8)
toDec([2,4,3,15,6,10,8,8,8,5,10,3], 16)

def toBase(input, baseA, baseB):
    dec = toDec(input, baseA)



0.3212 *3
0.9636
1.4040
0.404 *3
2.020
0.02 *3
0.1
0.1 *3
0.3 *3
1.3
1.3 *3

120011111...

# CORRECT !!! ################################################################
0.56 #base-8 multiplication, 10b10 = 12b8 
0.56*12
  50 60
5.6
0.75
6.2
7.14
0.14 * 12
    0.04 *10 / 8
        40 -> 50
        0.50
    0.1 *10 / 8
        10 -> 12
        1.2
    1.2 + 0.5
    1.7
0.7 * 12
7.0
10.6
0.6 *12
7.4
0.4*12
5.0

0.71875




