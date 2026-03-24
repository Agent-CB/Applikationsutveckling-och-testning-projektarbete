class ResultFormatter:
    def question_text(self, question):
        return question.text

    def option_text(self, index, option):
        return f"{index}: {option}"

    def invalid_input(self):
        return "Invalid input. Skipping question."

    def correct_answer(self):
        return "Correct!"

    def wrong_answer(self):
        return "Wrong!"

    def final_score(self, score):
        return f"Final score: {score}"
