import unittest

# Import test files
from test_cmd_a import TestCurrentCmdA
from test_cmd_b import TestCurrentCmdB
"""
# Import classes to be tested
from input_handler import InputHandler
from javascript_handler import JavascriptHandler
from dot_formatter import DotFormatter
from image_converter import ImageConverter
"""

def suite():
    theSuite = unittest.TestSuite()
    theSuite.addTest(unittest.makeSuite(TestCurrentCmdA))
    theSuite.addTest(unittest.makeSuite(TestCurrentCmdB))
    return theSuite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    # runner = unittest.TextTestRunner(descriptions=True, verbosity=2)
    test_suite = suite()
    runner.run(test_suite)

    # Run Coverage HTML Report
