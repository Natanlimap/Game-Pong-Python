import sys
sys.path.append("class/")
import home as Home
import game as Game

def main():
    Home.start()
    Game.start()

    print("{} fez {} ponto(s)!".format(Home.player, Game.COUNT))
main()