import sys
import os
import unittest

# Add src directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from print_r.print_r import app, appc, ppr

class TestPrintR(unittest.TestCase):
    def test_app(self):
        self.assertIsNone(app({"key": "value"}))

    def test_appc(self):
        self.assertIsNone(appc([1, 2, 3]))

    def test_ppr(self):
        self.assertIsNone(ppr({"key": ["value1", "value2"]}))

if __name__ == '__main__':
    unittest.main()
