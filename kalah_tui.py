from kalha import Kalha

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


def play_kalah_two_players(holes=6, seeds=4):
    print(color.BLUE + color.UNDERLINE + "let's play kalha game" + color.END)
    game = Kalha(holes, seeds)
    print(color.PURPLE + "Player 1 starts" + color.END)
    print(game)
    print(color.YELLOW + "- - - - - - - - - - - - -" + color.END)
    while not game.game_over():
        try:
            x = input(color.BLUE + "Enter your choice:   " + color.END)
            message = game.play(int(x))
            print(game)
            print(color.YELLOW + "- - - - - - - - - - - - -" + color.END)
            print(color.PURPLE + message + color.END)
        except ValueError:
            print(color.RED + "==>take a hole with almost 1 seed." + color.END)
        except IndexError:
            print(color.RED + f"==>the hole you want to coice is a number in range [0,{holes}]" + color.END)

    print(color.CYAN+"YAY!!!"+color.DARKCYAN+"WOW!!!"+color.CYAN+"COOL!!!"+color.END)
    print(game)
    print(color.DARKCYAN + "WELL DONE!" + color.END)


if __name__ == "__main__":
    play_kalah_two_players()