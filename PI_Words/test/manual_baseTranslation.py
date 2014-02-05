#!/usr/bin/python3
'''
Manual calculations for converting the base. Almost all are wrong!
'''

input = [1, 1]
expectedOutput = [2, 5]
assert cb(input, 2, 10, 2) == expectedOutput

# (1 / baseA)^(i + 1) * digits[i]
# (1 / 10)^(0+1) * 7 = 7/10
# (1 / 10)^(1+1) * 5 = 5/100
# (1 / baseB)^(i + 1) * output[i]
input = [7, 5]
'''
from RIGHT to left!
carry = 0
5 * 8 + carry = 40 = x
1. ith digit = x%baseA = 40%10 = 0
carry = 4.0
7 * 8 + carry = 56 + 4 = 60
x = 60
2. ith digit = 60%10 = 0
carry = 60/10 = 6
0*8 + carry = 6 = x
3. ith digit = x%baseA = 6%10 = 6
carry = 6/10 = 0.6

ith digit: (right to left)
3.2.1.
600
solution:
    0.6
base-10: 0.75 == base-8: 0.6
'''
# 0 * x ^ 1 + 1 * x ^ 2 + 2 * x ^ 3
expectedOutput = [6,0,0]
assert cb(input, 10, 8, 3) == expectedOutput


input = [5] # base 8
expect= [6,2,5] # base 10
'''
5 * 10 = 50 x
ith = 50%8 = 2
c = 50/8 = 6

2 * 10 = 20
ith = 20%8 = 4
c = 20/8 = 2

4*10 = 40
ith = 40%8= 0
c = 40/8 = 5

ALTERNATIVE:
0.5*10/8 = 0.625

'''
input = [0,6] # base 8 
expect= [0,9,3,7,5] # base 10
'''
0.06 * 10 = 0.6
0.6 / 8 = 0.075
0.075 *10 = 0.75
0.75/8 = 0.09375






.06 * 10 = 0.6
ith = 0.6
c = 0.075

0.6 10 + 0.075 = 6.075
ith = fmod(6.075,8)  = 6.075
c = 0.759375

6.075 *10 + 0.759375 =61.509375
ith = fmod(61.509375,8) = 5.509375
c = 61.509375/8 = 7.688672

5.509375 * 10 + 7.688672 = 62.782422



6 10 =60
ith =60%8 = 4
c=7

4 10 = 40
ith = 40*8 = 0
c = 5


'''

input = [5,6] # base 8
expect= [7,1,8,7,5] # base 10
carry = [6,2,5] # after 5


'''
1.25
0.56 * 10/8.0 *10 = 6.25
0.25 * 10 = 2.5
2.5 / 8 *10 = 3.125


6

0.06 * 10 = 0.6
0.6/8 = 0.075
0.075* 10 = 0.75
0.75/8 = 0.09375

5.6/8 = 0.7
7 *10 = 7
7/8 = 0.875
0.875*10 = 8.75
8.75/8 = 1.09375
0.09375*10 = 0.9375
0.9375/8 = 0.117188
0.117188*10 = 1.17188


1

'''
'''
0.71875*8 = 5.75
0.75*8 = 6.0

56
'''

input = [7] # base 10
expect= [5,4,6,3,1,4 ...] # base 8
'''
0.7*8 = 5.6
0.6*8 = 4.8
0.8*8 = 6.4
0.4*8 = 3.2
0.2*8 = 1.6
0.6*8 = 4.8
0.8*8 = 6.4
0.4*8 = 3.2
0.2*8 = 1.6
0.6*8 = 4.8

5463146314
'''

input = [7] # base 8
expect= [8,7,5] # base 10
'''
7 * 10 = 70
ith = 70%8 = 6
c = 8

6 * 10 = 60
ith =60%8 = 4
c = 7

40
ith = 40%8 = 0
c = 5
'''





input = [9]
'''
for i in range(precisionB):
    carry = 0
    x = input[i] * baseB + carry
'''

input = [15] # base 16 to 10 = 0.9375 according to http://baseconvert.com/
'''
15 * 10 = 1.5 / 16 = 0.09375
0.9375
0.5 * 10 = 5.0
15 *10^-1

0.15 * 10 = f


'''

input = [7,5] # base 10 to 8 = 0.6
'''
0.75 * 8 = 6.0
0.8*0.75 = 0.6
'''

input = [10, 10] # base 16 to 10 = 0.6640625
'''
0.aa * 10 = 100
0.54 * 10 = 

0.a * 10 = a / 16 = 0.625
0.625 * 10  = 


10 * 10 = 100 = x
ith = 100 % 16 = 4
c = 100 / 16 = 6.25
4 * 10 = 40 = x
ith = 40 %16 = 8
c = 40 / 16 = 2.5
8 * 10 = 80 = x 
ith = 80 % 16 = 0
c = 80/16= 5
'''



'''
0 c
15 * 10 + c = x = 150
ith[0] = 150 % 16 = 6
c = 150 / 16 = 9.375
out[0] = 9.375
'''
input = [7,5] # base 10 to 16 = 0.C according to http://baseconvert.com/
'''
5 * 16 +0 = 80
ith[0] =  80 % 10 = 0
c = 80 / 10 = 8
out[0] = 8

7 * 16 + 8 = 120
120 % 10 = 0
c = 12

16 * 0 + 12 = 12
12 %10 = 2
c = 1.2
'''

input = [4] # base 16 to 10 = 0.25 according to http://baseconvert.com/
'''
4 * 10 = 40
ith = 40 % 16 = 8
c =  40 / 16 = 2.5
out = 2.5
'''


cb = BaseTranslator.convertBase
# expectedOutput = [2,4,3,15,6,10,8,8,8,5]
assert cb(input, 10, 16, 11) == expectedOutput


input          = [1,4,1,5 ,9,2 ,6,5,3,5] # base 10 to 16
'''
5 * 16 = 80 = x
ith = 80 % 10 = 0
c = 8

3 * 16 = 48
ith = 48 % 10 = 8
c = 4.8


output = 8
'''
'''
5*16 + 0 = 80 x
80%10 =0 i
80/10 = 8 c
3*16 +8 = 48 + 8 = 56 x
56%10 = 6 i
56/10 = 5.6 c
5 * 16 + 5.6 = 85.6 x
85.6%10 = 5.6 i
85.6/10 = 8.56 c
6 * 16 + 8.56 = 96 + 8.56 = 104.56 x
104.56%10 = 4.56 i
104.56/10 = 10.456 c

'''


243156108885
1415926535
