import unittest
import first_none_repeating_character

class Test_FirstNone(unittest.TestCase):

    def test_firstnone(self):
        result = first_none_repeating_character.first_non_repeating_character('I came across/"jay"')
        self.assertEqual(result,'I')
    def test_firstnone1(self):
        result = first_none_repeating_character.first_non_repeating_character('')
        self.assertEqual(result,'')
    def test_firstnone2(self):
        result = first_none_repeating_character.first_non_repeating_character('--//\||<>l i  ')
        self.assertEqual(result,'\\')
    def test_firstnone3(self):
        result = first_none_repeating_character.first_non_repeating_character('eeeeee')
        self.assertEqual(result,'')
    


if __name__ == '__main__':
    unittest.main()