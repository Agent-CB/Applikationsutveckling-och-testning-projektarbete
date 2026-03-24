class QuizEngine:
    def __init__(
        self,
        question_repo,
        question_order_service,
        answer_parser,
        score_service,
        result_formatter,
        ui,
    ):
        self.question_repo = question_repo
        self.question_order_service = question_order_service
        self.answer_parser = answer_parser
        self.score_service = score_service
        self.result_formatter = result_formatter
        self.ui = ui

    def start(self):
        self.score_service.reset()
        questions = self.question_order_service.order_questions(
            self.question_repo.get_questions()
        )

        for question in questions:
            self.ui.show_text(self.result_formatter.question_text(question))

            for i, option in enumerate(question.options):
                self.ui.show_text(self.result_formatter.option_text(i, option))

            user_input = self.ui.read_input()
            answer_index = self.answer_parser.parse(user_input, len(question.options))
            if answer_index is None:
                self.ui.show_text(self.result_formatter.invalid_input())
                continue

            if question.is_correct(answer_index):
                self.score_service.add_point()
                self.ui.show_text(self.result_formatter.correct_answer())
            else:
                self.ui.show_text(self.result_formatter.wrong_answer())

        self.ui.show_text(
            self.result_formatter.final_score(self.score_service.get_score())
        )
