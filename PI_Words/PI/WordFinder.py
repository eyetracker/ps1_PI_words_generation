

class WordFinder:

    '''Given a String (the haystack) and an array of Strings (the needles),
    return a Map<String, Integer>, where keys in the map correspond to
    elements of needles that were found as substrings of haystack, and the
    value for each key is the lowest index of haystack at which that needle
    was found. A needle that was not found in the haystack should not be
    returned in the output map.

    @param haystack The string to search into.
    @param needles The array of strings to search for. This array is not
                   mutated.
    @return The list of needles that were found in the haystack.
    '''

    @staticmethod
    def getSubstrings(haystack, needles):
        # TODO: Implement (Problem 4.b)
        if not type(needles) is list:
            raise TypeError
        found_needles = {}
        for needle in needles:
            # print(haystack)
            # print(needle)
            foundindex = haystack.find(needle)
            if foundindex > -1:
                found_needles.update({needle: foundindex})
        return found_needles





