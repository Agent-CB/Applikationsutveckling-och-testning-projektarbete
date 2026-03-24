class AnswerParser:
    def parse(self, user_input, option_count):
        try:
            answer_index = int(user_input)
        except ValueError:
            return None

        if 0 <= answer_index < option_count:
            return answer_index

        return None
