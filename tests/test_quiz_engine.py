import unittest
from unittest.mock import Mock
from src.answer_parser import AnswerParser
from src.question import Question
from src.question_order_service import QuestionOrderService
from src.quiz_engine import QuizEngine
from src.result_formatter import ResultFormatter
from src.random_service import RandomService
from src.score_service import ScoreService


class TestQuizEngine(unittest.TestCase):
    def test_correct_answer_adds_point(self):
        mock_repo = Mock()
        mock_repo.get_questions.return_value = [Question("Q1", ["A", "B"], 0)]

        mock_ui = Mock()
        mock_ui.read_input.return_value = "0"

        score = ScoreService()
        engine = QuizEngine(
            mock_repo,
            QuestionOrderService(RandomService()),
            AnswerParser(),
            score,
            ResultFormatter(),
            mock_ui,
        )
        engine.start()

        self.assertEqual(score.get_score(), 1)

    def test_invalid_input_skips_question(self):
        mock_repo = Mock()
        mock_repo.get_questions.return_value = [Question("Q1", ["A", "B"], 0)]

        mock_ui = Mock()
        mock_ui.read_input.return_value = "abc"

        score = ScoreService()
        formatter = ResultFormatter()
        engine = QuizEngine(
            mock_repo,
            QuestionOrderService(RandomService()),
            AnswerParser(),
            score,
            formatter,
            mock_ui,
        )
        engine.start()

        self.assertEqual(score.get_score(), 0)
        mock_ui.show_text.assert_any_call(formatter.invalid_input())

    def test_wrong_answer_shows_wrong_message(self):
        mock_repo = Mock()
        mock_repo.get_questions.return_value = [Question("Q1", ["A", "B"], 0)]

        mock_ui = Mock()
        mock_ui.read_input.return_value = "1"

        formatter = ResultFormatter()
        engine = QuizEngine(
            mock_repo,
            QuestionOrderService(RandomService()),
            AnswerParser(),
            ScoreService(),
            formatter,
            mock_ui,
        )
        engine.start()

        mock_ui.show_text.assert_any_call(formatter.wrong_answer())


if __name__ == "__main__":
    unittest.main()
