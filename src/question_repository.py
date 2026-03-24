try:
    from .question import Question
except ImportError:
    from question import Question


class QuestionRepository:
    def get_questions(self):
        return [
            Question("What is the capital of France?", ["Paris", "London", "Berlin"], 0),
            Question("What is 2 + 2?", ["3", "4", "5"], 1),
            Question(
                "Which planet is known as the Red Planet?",
                ["Earth", "Mars", "Jupiter"],
                1,
            ),
        ]
