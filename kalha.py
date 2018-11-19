class Kalha:
    def __init__(self, holes, seeds):
        self.player = 0
        self.bank = [0, 0]
        self.holes = holes
        self.now = [[],[]]
        for j in range(2):
            for i in range(holes):
                self.now[j].append(seeds)
        self.winnerr = 10

    def __repr__(self):
        show = ' '
        for i in range(self.holes):
            show += str(self.now[0][self.holes-1-i])
        show += '\n'
        show += str(self.bank[0]) + " " * self.holes + str(self.bank[1]) + '\n' + ' '
        for i in range(self.holes):
            show += str(self.now[1][self.holes-1-i])
        return show

    def __str__(self):
        show = 'Player1: '
        for i in range(self.holes):
            show += str(self.now[0][self.holes-1-i])
        show += '\n        '
        show += str(self.bank[0]) + " " * self.holes + str(self.bank[1]) + '\n' + 'Player2: '
        for i in range(self.holes):
            show += str(self.now[1][self.holes-1-i])
        return show


    def play(self, hole):
        if self.winnerr != 10:
            return "Player {} wins.".format(self.winnerr+1)
        if hole > self.holes or hole < 1:
            raise IndexError
        # hole = hole - 1
        if self.now[self.player][hole - 1] == 0:
            raise ValueError
        stones = self.now[self.player][hole - 1]
        self.now[self.player][hole - 1] = 0
        play_er = self.player
        flag = 0
        while stones:
            if hole < self.holes:
                self.now[play_er][hole] += 1
                hole += 1
            else:
                if play_er == self.player:
                    self.bank[play_er] += 1
                else:
                    stones += 1
                hole = 0
                if stones - 1 > 0:
                    play_er = 1 - play_er
                flag = 1
            stones = stones - 1
        if not any(self.now[self.player]):
            self.player = 1-self.player
            return self.end_function(1-self.player)#"Player 2 plays next" if self.player else "Player 1 plays next"

        helper = self.help_function(1-self.player)
        if not helper is 10:
            return helper

        if play_er == self.player:
            if hole != 0 and self.now[play_er][hole - 1] == 1 and self.now[1-play_er][self.holes - hole] != 0:
                self.bank[play_er] += 1
                self.now[play_er][hole - 1] = 0
                self.bank[play_er] += self.now[1 - play_er][(self.holes - hole)]
                self.now[1 - play_er][self.holes - hole] = 0
        if hole != 0 or play_er != self.player:
            self.player = 1 - self.player
        return "Player 2 plays next" if self.player else "Player 1 plays next"


    def status(self):
        listt = []
        for j in range(2):
            for i in range(self.holes):
                listt.append(self.now[j][i])
            listt.append([self.bank[j]])
        return listt


    def winner(self):
        return self.winnerr


    def help_function(self, player):
        if not any(self.now[player]):  # 1-self.player]):
            #self.player = 1 - self.player
            for i in range(self.holes):
                self.bank[1 - player] += self.now[1 - player][i]
                self.now[1-player][i] = 0
            self.player = 1 - self.player
            if self.bank[self.player] > self.bank[1 - self.player]:
                self.winnerr = self.player
                return "Player {} wins.".format(self.player + 1)
            elif self.bank[1 - self.player] > self.bank[self.player]:
                self.winnerr = (1 - self.player) + 1
                return "Player {} wins.".format((1 - self.player) + 1)
            else:
                self.winnerr = None
                return "Tie"
        else:
            return 10

    def end_function(self, player):
        if any(self.now[1-player]):
            self.player = 1-self.player
            for i in range(self.holes):
                self.bank[1 - player] += self.now[1 - player][i]
                self.now[1-player][i] = 0
            self.player = 1 - self.player
            if self.bank[self.player] > self.bank[1 - self.player]:
                self.winnerr = self.player
                return "Player {} wins.".format(self.player + 1)
            elif self.bank[1 - self.player] > self.bank[self.player]:
                self.winnerr = (1 - self.player) + 1
                return "Player {} wins.".format((1 - self.player) + 1)
            else:
                self.winnerr = None
                return "Tie"