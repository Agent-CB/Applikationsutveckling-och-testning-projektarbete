import unittest
from src.score_service import ScoreService


class TestScoreService(unittest.TestCase):
    def test_add_point(self):
        score = ScoreService()
        score.add_point()
        self.assertEqual(score.get_score(), 1)

    def test_reset_clears_score(self):
        score = ScoreService()
        score.add_point()
        score.reset()
        self.assertEqual(score.get_score(), 0)


if __name__ == "__main__":
    unittest.main()
