import unittest
from src.answer_parser import AnswerParser


class TestAnswerParser(unittest.TestCase):
    def test_parse_returns_index_for_valid_number(self):
        parser = AnswerParser()
        self.assertEqual(parser.parse("1", 3), 1)

    def test_parse_returns_none_for_non_numeric_input(self):
        parser = AnswerParser()
        self.assertIsNone(parser.parse("abc", 3))

    def test_parse_returns_none_for_out_of_range_value(self):
        parser = AnswerParser()
        self.assertIsNone(parser.parse("5", 3))


if __name__ == "__main__":
    unittest.main()
