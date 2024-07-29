import sys
import os
import unittest

from print_r import app, appc, ppr

class TestPrintR(unittest.TestCase):
    def test_app(self):
        self.assertIsNone(app({"key": "value"}))

    def test_appc(self):
        self.assertIsNone(appc([1, 2, 3]))

    def test_ppr(self):
        self.assertIsNone(ppr({"key": ["value1", "value2"]}))

if __name__ == '__main__':
    unittest.main()
