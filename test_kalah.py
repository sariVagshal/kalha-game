import unittest
#from kalha_tests.kalha import Kalha
from kalha import Kalha
#from ..kalha_tests import kalha as Kalha
#import .kalha as Kalha

class KalhaTestCase(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_simple(self):
        game = Kalha(6, 4)
        self.assertEqual(game.status(), [4,4,4,4,4,4,[0],4,4,4,4,4,4,[0],])
        self.assertEqual(game.play(1), "Player 2 plays next")
        self.assertEqual(game.status(), [0,5,5,5,5,4,[0],4,4,4,4,4,4,[0],])
        self.assertEqual(game.play(4), "Player 1 plays next")
        self.assertEqual(game.status(), [1,5,5,5,5,4,[0],4,4,4,0,5,5,[1],])
        self.assertEqual(game.play(1), "Player 2 plays next")
        self.assertEqual(game.status(), [0,6,5,5,5,4,[0],4,4,4,0,5,5,[1],])
        self.assertRaises(IndexError,game.play,7)
        self.assertRaises(ValueError,game.play,4)

    def test_game1(self):
        game = Kalha(6, 6)
        self.assertEqual(game.status(), [6, 6, 6, 6, 6, 6, [0], 6, 6, 6, 6, 6, 6, [0], ])
        self.assertEqual(game.play(2), "Player 2 plays next")
        self.assertEqual(game.status(), [6, 0, 7, 7, 7, 7, [1], 7, 6, 6, 6, 6, 6, [0], ])
        self.assertEqual(game.play(1), "Player 1 plays next")
        self.assertEqual(game.play(4), "Player 2 plays next")
        self.assertEqual(game.status(), [7, 0, 7, 0, 8, 8, [2], 1, 8, 8, 8, 7, 7, [1],])
        self.assertEqual(game.play(2), "Player 1 plays next")
        self.assertEqual(game.play(1), "Player 2 plays next")
        self.assertEqual(game.status(), [0, 2, 9, 1, 9, 9, [3], 2, 1, 9, 9, 8, 8, [2], ])
        self.assertEqual(game.play(2), "Player 1 plays next")
        self.assertEqual(game.play(5), "Player 2 plays next")
        self.assertEqual(game.status(), [0, 2, 9, 1, 0, 10, [14], 3, 1, 11, 10, 9, 0, [2], ])
        self.assertEqual(game.play(5), "Player 1 plays next")
        self.assertEqual(game.play(6), "Player 2 plays next")
        self.assertEqual(game.status(), [2, 4, 11, 3, 1, 0, [15], 5, 2, 12, 11, 1, 2, [3], ])
        self.assertEqual(game.play(5), "Player 1 plays next")
        self.assertEqual(game.play(4), "Player 1 plays next")
        self.assertEqual(game.play(6), "Player 1 plays next")
        self.assertEqual(game.play(5), "Player 1 plays next")
        self.assertEqual(game.play(6), "Player 1 plays next")
        self.assertEqual(game.play(2), "Player 2 plays next")
        self.assertEqual(game.status(), [2, 0, 12, 1, 1, 0, [25], 0, 2, 12, 11, 0, 3, [3], ])
        self.assertEqual(game.play(2), "Player 1 plays next")
        self.assertEqual(game.play(3), "Player 2 plays next")
        self.assertEqual(game.status(), [3, 0, 0, 2, 2, 1, [28], 1, 1, 14, 13, 0, 4, [3], ])
        self.assertEqual(game.play(1), "Player 1 plays next")
        self.assertEqual(game.play(6), "Player 1 plays next")
        self.assertEqual(game.play(5), "Player 1 plays next")
        self.assertEqual(game.play(6), "Player 1 plays next")
        self.assertEqual(game.play(4), "Player 2 plays next")
        self.assertEqual(game.status(), [3, 0, 0, 0, 1, 0, [32], 0, 2, 14, 13, 0, 4, [3], ])
        self.assertEqual(game.play(2), "Player 1 plays next")
        self.assertEqual(game.play(1), "Player 1 wins")
        self.assertEqual(game.status(), [0, 1, 1, 0, 1, 0, [48], 0, 0, 0, 14, 0, 4, [3], ])
        self.assertEqual(game.play(1), "Game Over")

    def test_game2(self):
        game = Kalha(6, 6)
        self.assertEqual(game.play(2), "Player 2 plays next")
        self.assertEqual(game.play(6), "Player 1 plays next")
        self.assertEqual(game.play(1), "Player 2 plays next")
        self.assertEqual(game.status(), [0, 2, 9, 9, 9, 8, [2], 8, 6, 6, 6, 6, 0, [1], ])
        self.assertEqual(game.play(5), "Player 1 plays next")
        self.assertEqual(game.play(5), "Player 2 plays next")
        self.assertEqual(game.status(), [2, 3, 10, 10, 0, 9, [3], 9, 7, 7, 7, 1, 2, [2], ])
        self.assertEqual(game.play(6), "Player 1 plays next")
        self.assertEqual(game.play(2), "Player 2 plays next")
        self.assertEqual(game.status(), [3, 0, 11, 11, 0, 9, [11], 9, 0, 7, 7, 1, 0, [3], ])
        self.assertEqual(game.play(5), "Player 1 plays next")
        self.assertEqual(game.play(3), "Player 2 plays next")
        self.assertEqual(game.status(), [0, 0, 0, 12, 1, 10, [14], 10, 1, 8, 8, 1, 0, [7], ])
        self.assertEqual(game.play(5), "Player 1 plays next")
        self.assertEqual(game.play(6), "Player 2 plays next")
        self.assertEqual(game.status(), [1, 1, 0, 12, 1, 0, [25], 11, 2, 9, 0, 1, 1, [8], ])
        self.assertEqual(game.play(1), "Player 1 plays next")
        self.assertEqual(game.play(5), "Player 1 plays next")
        self.assertEqual(game.play(6), "Player 1 plays next")
        self.assertEqual(game.play(4), "Player 1 wins")
        self.assertEqual(game.status(), [3, 3, 2, 0, 1, 1, [40], 1, 4, 0, 2, 3, 3, [9], ])

    def test_game3(self):
        game = Kalha(6, 6)
        self.assertEqual(game.play(2), "Player 2 plays next")
        self.assertEqual(game.play(1), "Player 1 plays next")
        self.assertEqual(game.play(4), "Player 2 plays next")
        self.assertEqual(game.status(), [7, 0, 7, 0, 8, 8, [2], 1, 8, 8, 8, 7, 7, [1], ])
        self.assertEqual(game.play(1), "Player 1 plays next")
        self.assertEqual(game.play(1), "Player 2 plays next")
        self.assertEqual(game.status(), [0, 1, 8, 1, 9, 9, [3], 1, 9, 8, 8, 7, 7, [1], ])
        self.assertEqual(game.play(2), "Player 1 plays next")
        self.assertEqual(game.play(6), "Player 2 plays next")
        self.assertEqual(game.status(), [2, 3, 9, 2, 9, 0, [4], 2, 1, 10, 10, 9, 9, [2], ])
        self.assertEqual(game.play(1), "Player 1 plays next")
        self.assertEqual(game.play(1), "Player 2 plays next")
        self.assertEqual(game.status(), [0, 4, 10, 2, 9, 0, [4], 0, 2, 11, 10, 9, 9, [2], ])
        self.assertEqual(game.play(2), "Player 1 plays next")
        self.assertEqual(game.play(5), "Player 2 plays next")
        self.assertEqual(game.status(), [0, 4, 10, 2, 0, 1, [16], 1, 1, 13, 12, 10, 0, [2], ])
        self.assertEqual(game.play(1), "Player 1 plays next")
        self.assertEqual(game.play(6), "Player 1 plays next")
        self.assertEqual(game.play(4), "Player 2 plays next")
        self.assertEqual(game.status(), [0, 4, 10, 0, 1, 0, [18], 0, 2, 13, 12, 10, 0, [2], ])
        self.assertEqual(game.play(2), "Player 1 plays next")
        self.assertEqual(game.play(5), "Player 2 plays next")
        self.assertEqual(game.status(), [0, 4, 10, 0, 0, 0, [19], 0, 0, 14, 13, 10, 0, [2], ])
        self.assertEqual(game.play(3), "Player 1 plays next")
        self.assertEqual(game.play(6), "Player 1 plays next")
        self.assertEqual(game.play(2), "Player 1 plays next")
        self.assertEqual(game.play(6), "Player 1 plays next")
        self.assertEqual(game.play(5), "Player 1 plays next")
        self.assertEqual(game.play(6), "Player 1 plays next")
        self.assertEqual(game.play(3), "Player 1 wins")
        self.assertEqual(game.status(), [2, 0, 0, 3, 1, 1, [38], 2, 2, 2, 16, 0, 2, [3], ])

    def test_simulate(self):
        dic_p1 = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6}
        dic_p2 = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6}
        path = "simulate.txt"
        game = Kalha(6,6)
        with open(path, 'r') as f:
            content = f.read().splitlines()
        for line in content:
            self.assertFalse(game.winnerr)
            print(line)
            line = line[line.find('.')+2:]
            p1, p2 = line.split()
            #p1
            prev = game.bank[0]
            if p1.find('(')!=-1:
                actions, bank = p1.split('(')
                bank = bank.split(')')
                bank = int(bank[0][1:])
            else:
                actions = p1
                bank = 0
            if actions.find('-') != -1:
                actions=actions.split('-')
            else:
                actions=[actions]
            for i in actions:
                game.play(dic_p1[i])
            self.assertEqual(bank,game.bank[0]-prev)
            # p2
            prev = game.bank[1]
            if p2.find('(')!=-1:
                actions, bank = p2.split('(')
                bank = bank.split(')')
                bank = int(bank[0][1:])
            else:
                actions = p2
                bank = 0
            if actions.find('-') != -1:
                actions=actions.split('-')
            else:
                actions=[actions]
            for i in actions:
                game.play(dic_p2[i])
            self.assertEqual(bank, game.bank[1] - prev)
        self.assertTrue(game.winnerr)




if __name__ == '__main__':
    unittest.main()