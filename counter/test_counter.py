"""Write a unit test to verify that Counter is a singleton.

   Also verify that all instances share the same count
   and that the count is not reset to 0 when you invoke 
   count = Counter() 
   after the first time.

   You can use pytest or unittest.
"""

import unittest
from counter import Counter


class Singleton(unittest.TestCase):
    def test_counter(self):
        counter1 = Counter()
        counter2 = Counter()
        counter1.increment()
        self.assertEqual(counter1, counter2)
        self.assertTrue(counter1 is counter2)
