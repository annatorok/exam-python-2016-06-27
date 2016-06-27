import unittest
import third

class Test_count_letter_in_string(unittest.TestCase):

    def test_count_if_empty_letter_empty_string(self):
        self.assertEqual(third.count_letter_in_string('', ''), 0)

    def test_count_if_empty_string(self):
        self.assertEqual(third.count_letter_in_string('', 'b'), 0)

    def test_count_with_int(self):
        self.assertEqual(third.count_letter_in_string(3483, '3'), 0)

    def test_count_with_float(self):
        self.assertEqual(third.count_letter_in_string(129.5, '2'), 0)

    def test_count_if_string(self):
        self.assertEqual(third.count_letter_in_string('almafa', 'a'), 3)

    def test_count_if_list(self):
        self.assertEqual(third.count_letter_in_string([1,4,8,2,8], '8'), 0)

    def test_count_if_boolean(self):
        self.assertEqual(third.count_letter_in_string(True, 'u'), 0)

    def test_count_with_hypen_letters(self):
        self.assertEqual(third.count_letter_in_string('lomha-macska', 'a'), 3)

    def test_count_with_uppercase_letters(self):
        self.assertNotEqual(third.count_letter_in_string('asztalavisZTA', 'a'), 4)

    def test_count_if_letter_more_than_one_character(self):
        self.assertEqual(third.count_letter_in_string('macska', 'ka'), 0)

if __name__ == '__main__':
    unittest.main()
