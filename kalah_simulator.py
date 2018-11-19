from kalha import Kalha

def parse_game(lines):
    steps = []
    dic = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, }
    for line in lines:
        line = line[line.find('.') + 2:]
        two_players = line.split()
        if not type(two_players) is list:
            two_players = [two_players]
        for i in range(len(two_players)):
            if two_players[i].find('(') != -1:
                actions, bank = two_players[i].split('(')
                bank = bank.split(')')
                bank = bank[0]#(INT)#[1:])
            else:
                actions = two_players[i]
                bank = "+0"
            if actions.find('-') != -1:
                actions = actions.split('-')
            else:
                actions = [actions]
            for act in actions:
                steps.append(dic[act])
            steps.append(bank)
    return steps

def simulate_game(holes, seeds, steps)->(str, str):
    game = Kalha(6, 6)
    prev = game.bank[game.player]
    for step in steps:
        if '+' in str(step):
            print(step, "==", game.bank[1-game.player], "-", prev)
            assert int(step[1:]) == game.bank[1-game.player]-prev
            prev = game.bank[game.player]
        else:
            yield (game.play(step),game.status())
    #return game.winnerr()


def render_game(holes, seeds, steps):
    simulate_game(holes, seeds, steps)
    return "finish game"

if __name__ == "__main__":
    with open(f"data/game_3.txt") as f:
        lines = f.read().splitlines()
    steps = parse_game(lines)
    print(render_game(6, 6, steps))
