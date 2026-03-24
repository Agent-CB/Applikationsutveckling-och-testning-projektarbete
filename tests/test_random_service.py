import unittest
from src.random_service import RandomService


class TestRandomService(unittest.TestCase):
    def test_next_returns_within_range(self):
        random_service = RandomService()
        value = random_service.next(5)
        self.assertTrue(0 <= value < 5)

    def test_next_with_one_returns_zero(self):
        random_service = RandomService()
        value = random_service.next(1)
        self.assertEqual(value, 0)


if __name__ == "__main__":
    unittest.main()
