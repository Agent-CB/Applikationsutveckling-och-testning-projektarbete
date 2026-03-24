class ScoreService:
    def __init__(self):
        self.score = 0

    def add_point(self):
        self.score += 1

    def get_score(self):
        return self.score

    def reset(self):
        self.score = 0
