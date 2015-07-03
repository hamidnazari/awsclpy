import unittest

class TestUtils(unittest.TestCase):
    def setUp(self):
        from awsclpy.utils import log, flatten
        self.log = log
        self.flatten = flatten

    def test_flatten(self):
        flatted = self.flatten(['a', 'b', ['c'], ['d']])
        flatted = list(flatted)
        self.assertEqual(flatted, ['a', 'b', 'c', 'd'])
