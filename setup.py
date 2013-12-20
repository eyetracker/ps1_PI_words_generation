#!/usr/bin/python3

from setuptools import setup
from setuptools import find_packages
from setuptools.command.test import test as TestCommand
import sys

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True
    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)

class Tox(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True
    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import tox
        errcode = tox.cmdline(self.test_args)
        sys.exit(errcode)

setup(
        name='PiWords',
        version='0.1',
        author='Arthur "freeo" Jaron',
        description='''MIT 6-005 Problem Set 1: PI English Words Generator for
        learning test-driven-development.''',
        packages=find_packages(),
        # for testing! Uses default pyunit (unittest).
        # test_suite="PI_Words.test",
        # test_suite="pytest",
        # test_require="pytest",
        tests_require=['tox'],
        cmdclass = {'test': Tox},
        # tests_require=['pytest'],
        # cmdclass = {'test': PyTest},
        )

# http://peak.telecommunity.com/DevCenter/setuptools#test
# Abstract example for setting test_suite:
# test_suite = "my_package.tests.test_all"
# If the named suite is a package, any submodules and subpackages are
# recursively added to the overall test suite.
