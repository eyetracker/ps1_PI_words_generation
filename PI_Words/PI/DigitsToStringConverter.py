
class DigitsToStringConverter:
    ''' Given a list of digits, a base, and an mapping of digits of that base to
    chars, convert the list of digits into a character string by applying the
    mapping to each digit in the input.

    If digits[i] >= base or digits[i] < 0 for any i, consider the input
    invalid, and return null.
    If alphabet.length != base, consider the input invalid, and return null.

    @param digits A list of digits to encode. This object is not mutated.
    @param base The base the digits are encoded in.
    @param alphabet The mapping of digits to chars. This object is not
                    mutated.
    @return A String encoding the input digits with alphabet.
    '''

    @staticmethod
    def convertDigitsToString(digits, base, alphabet):
        '''
        Problem 3.b
        TESTS (Problem 3.a): ../test/test_DigitsToStringConverter.py|5|
        '''
        #catch invalid inputs, return 0
        for i in digits:
            if i > base or i < 0:
                return 0
        if len(alphabet) != base:
            return 0

        # Map digits by alphabet
        output = []
        for i in digits:
            output.append(alphabet[i])
        return ''.join(output)




