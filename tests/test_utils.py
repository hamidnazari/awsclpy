import unittest
from mock import mock_open, patch
from datetime import datetime


class TestUtils(unittest.TestCase):
    def setUp(self):
        from awsclpy.utils import log, flatten
        self.log = log
        self.flatten = flatten

    def test_log(self):
        logdir = './logs'
        now = datetime.now()
        date = now.strftime('%Y%m%d')

        mopen = mock_open()
        with patch('awsclpy.utils.open', mopen, create=True):
            self.log('test message', now, logdir)

        mopen.assert_called_once_with('%s/%s' % (logdir, date), 'a')

    def test_flatten(self):
        flatted = self.flatten(['a', 'b', ['c'], ['d']])
        flatted = list(flatted)
        self.assertEqual(flatted, ['a', 'b', 'c', 'd'])

    def test_flatten_first_half_empty(self):
        flatted = self.flatten([['c'], ['d']])
        flatted = list(flatted)
        self.assertEqual(flatted, ['c', 'd'])

    def test_flatten_second_half_empty(self):
        flatted = self.flatten(['a', 'b'])
        flatted = list(flatted)
        self.assertEqual(flatted, ['a', 'b'])

    def test_flatten_empty(self):
        flatted = self.flatten([])
        flatted = list(flatted)
        self.assertEqual(flatted, [])

    def test_flatten_string(self):
        flatted = self.flatten('test')
        flatted = list(flatted)
        self.assertEqual(flatted, ['t', 'e', 's', 't'])

    def test_flatten_string_array(self):
        flatted = self.flatten(['test'])
        flatted = list(flatted)
        self.assertEqual(flatted, ['test'])

    def test_flatten_numbers(self):
        flatted = self.flatten([1, 2, [3.0, 4.0], 5.0, 6])
        flatted = list(flatted)
        self.assertEqual(flatted, [1, 2, 3.0, 4.0, 5.0, 6])

    def test_flatten_mixed(self):
        flatted = self.flatten(['pi', 3.14])
        flatted = list(flatted)
        self.assertEqual(flatted, ['pi', 3.14])

    def test_flatten_deep_mixed(self):
        flatted = self.flatten([[1, 2, ['pi']], 3.14, [[[[[[5]]]], 4, [[6]]]]])
        flatted = list(flatted)
        self.assertEqual(flatted, [1, 2, 'pi', 3.14, 5, 4, 6])
