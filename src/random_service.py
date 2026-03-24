import random


class RandomService:
    def next(self, max_value):
        return random.randint(0, max_value - 1)
