from PI_Words.PI.WordFinder import WordFinder
import pytest

getSubstrings = WordFinder.getSubstrings

def test_EmptyHaystack():
    haystack = ""
    needles = ['abc']
    assert {} == getSubstrings(haystack, needles)

def test_EmptyNeedles():
    haystack = "abc"
    needles = []
    assert {} == getSubstrings(haystack, needles)

def test_InvalidNeedles():
    haystack = "abc"
    needles = None
    with pytest.raises(TypeError):
        result = getSubstrings(haystack, needles)

def test_basicGetSubstrings():
    haystack = "abcde"
    needles = ["ab", "abc", "de", "fg"]

    expectedOutput = {}
    expectedOutput.update({"ab": 0})
    expectedOutput.update({"abc": 0})
    expectedOutput.update({"de": 3})

    assert expectedOutput == getSubstrings(haystack, needles)

def test_MultipleOccurence():
    haystack = "abcabc"
    needles = ["ab", "abc", "cab", "fg"]

    expectedOutput = {}
    expectedOutput.update({"ab": 0})
    expectedOutput.update({"abc": 0})
    expectedOutput.update({"cab": 2})

    assert expectedOutput == getSubstrings(haystack, needles)

def test_EmptyReturn():
    haystack = "abcabc"
    needles = ["foo", "bar", "gnar", "klo"]
    expectedOutput = {}

    assert expectedOutput == getSubstrings(haystack, needles)

