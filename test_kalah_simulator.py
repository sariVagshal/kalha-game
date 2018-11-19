import unittest
import logging
from kalah_simulator import parse_game, simulate_game

logger = logging.getLogger(__name__)
class KalahSimulatorTestCase(unittest.TestCase):

    def test_simulation(self):
        path = "data/game_3.txt"  # "simulate.txt"#
        message, status = "",""
        with open(path, 'r') as f:
            lines = f.read().splitlines()
        steps = parse_game(lines)
        for message, status in simulate_game(6, 6, steps):
            logger.debug(message, status)
        self.assertEqual((0, 0, 0, 0, 0, 0, 38, 0, 0, 0, 0, 0, 0, 34), status)
        self.assertEqual(message, "Player 1 wins.")


if __name__ == '__main__':
    unittest.main()
