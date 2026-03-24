try:
    from .answer_parser import AnswerParser
    from .console_ui import ConsoleUI
    from .question_order_service import QuestionOrderService
    from .question_repository import QuestionRepository
    from .quiz_engine import QuizEngine
    from .random_service import RandomService
    from .result_formatter import ResultFormatter
    from .score_service import ScoreService
except ImportError:
    from answer_parser import AnswerParser
    from question_repository import QuestionRepository
    from console_ui import ConsoleUI
    from question_order_service import QuestionOrderService
    from quiz_engine import QuizEngine
    from random_service import RandomService
    from result_formatter import ResultFormatter
    from score_service import ScoreService


def main():
    repo = QuestionRepository()
    random_service = RandomService()
    question_order_service = QuestionOrderService(random_service)
    answer_parser = AnswerParser()
    score = ScoreService()
    result_formatter = ResultFormatter()
    ui = ConsoleUI()

    engine = QuizEngine(
        repo,
        question_order_service,
        answer_parser,
        score,
        result_formatter,
        ui,
    )
    engine.start()


if __name__ == "__main__":
    main()
