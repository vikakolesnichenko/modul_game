from models import *
import exceptions
from settings import *


if __name__ == '__main__':

    def play():
        name = str(input("Please, enter your name: \n"))
        lives = PLAYER_LIVES
        enem_life = ENEMY_LEVEL
        enem_level = ENEMY_LEVEL
        player = Player(name, lives)
        enemy = Enemy(enem_life, enem_level)

        begin_of_game = input('Enter "start" to start the game: \n')

        if begin_of_game == "start":
            print(f"{name}, welcome to the game")
            while True:
                try:
                    player.attack(enemy)
                    player.defence(enemy)
                    if player.attack(enemy) == "You attacked successfully":
                        enemy.decrease_lives()
                except exceptions.EnemyDown:
                    player.score += 5
                    print(f"Your score: {player.score}")
                    enemy.level += 1
                    enemy.live = enemy.level
                    print(f"Enemy status: {enemy.live}, {enemy.level}")

    try:
        play()
    except exceptions.GameOver:\
            print("It's all")
    finally:
        print("Good bye")

