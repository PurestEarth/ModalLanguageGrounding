import unittest


class MyTestCase(unittest.TestCase):
    def test_andS(self):
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()