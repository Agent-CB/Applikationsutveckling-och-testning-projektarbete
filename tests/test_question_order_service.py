import unittest

from src.question import Question
from src.question_order_service import QuestionOrderService


class FakeRandomService:
    def __init__(self, values):
        self.values = list(values)

    def next(self, max_value):
        return self.values.pop(0)


class TestQuestionOrderService(unittest.TestCase):
    def test_order_questions_keeps_same_items(self):
        questions = [
            Question("Q1", ["A"], 0),
            Question("Q2", ["B"], 0),
            Question("Q3", ["C"], 0),
        ]
        service = QuestionOrderService(FakeRandomService([1, 0]))

        ordered_questions = service.order_questions(questions)

        self.assertEqual(
            [question.text for question in ordered_questions],
            ["Q3", "Q1", "Q2"],
        )

    def test_order_questions_returns_copy_for_empty_input(self):
        service = QuestionOrderService(FakeRandomService([]))
        self.assertEqual(service.order_questions([]), [])


if __name__ == "__main__":
    unittest.main()
