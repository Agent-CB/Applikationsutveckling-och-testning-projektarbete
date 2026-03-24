import unittest
from src.question_repository import QuestionRepository


class TestQuestionRepository(unittest.TestCase):
    def test_get_questions_returns_list(self):
        repo = QuestionRepository()
        questions = repo.get_questions()
        self.assertGreater(len(questions), 0)

    def test_get_questions_returns_question_objects(self):
        repo = QuestionRepository()
        question = repo.get_questions()[0]
        self.assertTrue(hasattr(question, "text"))
        self.assertTrue(hasattr(question, "options"))
        self.assertTrue(hasattr(question, "correct_index"))


if __name__ == "__main__":
    unittest.main()
