class QuestionOrderService:
    def __init__(self, random_service):
        self.random_service = random_service

    def order_questions(self, questions):
        ordered_questions = list(questions)

        for index in range(len(ordered_questions) - 1, 0, -1):
            swap_index = self.random_service.next(index + 1)
            ordered_questions[index], ordered_questions[swap_index] = (
                ordered_questions[swap_index],
                ordered_questions[index],
            )

        return ordered_questions
