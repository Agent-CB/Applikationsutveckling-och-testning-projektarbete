import unittest

from src.question import Question
from src.result_formatter import ResultFormatter


class TestResultFormatter(unittest.TestCase):
    def test_question_text_returns_question_prompt(self):
        formatter = ResultFormatter()
        question = Question("Capital?", ["Paris"], 0)
        self.assertEqual(formatter.question_text(question), "Capital?")

    def test_option_text_formats_index_and_option(self):
        formatter = ResultFormatter()
        self.assertEqual(formatter.option_text(2, "Mars"), "2: Mars")

    def test_final_score_formats_message(self):
        formatter = ResultFormatter()
        self.assertEqual(formatter.final_score(2), "Final score: 2")


if __name__ == "__main__":
    unittest.main()
