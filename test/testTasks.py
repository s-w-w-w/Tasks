#!/usr/bin/env python3

import sys
from pathlib import Path
# add parent path of lib dir to path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import unittest

# display path
from lib.Tasks import *

class TestTasks(unittest.TestCase): 

    """
    Sample test
    """
    def test_something(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

