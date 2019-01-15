import unittest
from main import Magic


class TestMagic(unittest.TestCase):
    """Test class for GuessNumber"""

    def setUp(self):
        """Setup method for the test case class"""
        self.new_magic = Magic(username="Tom")

    def test_generate_random(self):
        """Method that test generated numbers"""
        res = Magic.generate_random_answer(self)
        self.assertTrue(type(res), str)

    def test_show_progress(self):
        """Method that test generated numbers"""
        res = Magic.show_progress(self)
        self.assertTrue(type(res), str)
        self.assertTrue(res, "In progress,kindly wait.....")


if __name__ == '__main__':
    unittest.main()
