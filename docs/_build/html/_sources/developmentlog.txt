1. Pi Generation
================

Using the Bailey-Borwein-Plouffe formula to generate an arbitrary number of
pi's digits.

1.  Carefully look at the specification of the method you are looking to
    implement.
2.  Write a battery of tests to test the method you are about to write,
    checking all of the edge conditions for the specification.
3.  Write the actual method we specified.

The 'assert' statement
----------------------
Python testing is limited by one **assertion** per function! This means, that
the function fails on the first assert failure. This is because `assert`
returns `-1` from the failed test function.  It can be concluded, that
assertion statements **need** to be grouped in very similar statements!  

About specifications
--------------------
Main specification belongs under the function, but the role of specifications
hints inbetween the test cases remains unresolved for now. It seems useful to
have some more information about a tests background, but the work gets doubled
by that. I link between the test cases and the full specification would be
useful.

New:
Chained OR operators:
    if a | b | m < 0:

Relearned:
    The power operator: ******

21.12.2013
----------
**Porting java to python:**
Look out for

    for (int i; i <= k; i++)
    for i in range(k+1)

default python ranges are short of one - cost me much time to find this.

**Vim configuration**
Wasting much time to configure everything in Vim, just to encounter an exceptional case, which breaks all the nice setups, which often try to avoid the console.

    Embrace the console! Though async processing would be very nice...

22.12.2013 
----------
a ** b is slow... cProfile shows, that this is a real bottleneck, whichs takes 90% of the computing time - annoying.
Tested alternatives:

    math.pow(a, b) - no improvement
    power = eval('a'+'*a'*(b-1)) - works, but MemoryError because of high 'b'

Great idea from Game development:

    power tables! Pre-calculated power values!
