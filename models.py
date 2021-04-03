import settings
import random
from exceptions import EnemyDown
from exceptions import GameOver

class Enemy:
    def __init__(self, level, lives):
        self.level = settings.ENEMY_LEVEL
        self.lives = lives


    @staticmethod
    def select_attack():
        number_attack = random.randrange(1, 4)
        return (number_attack)

    def decrease_lives(self):
        self.lives -= 1
        try:
            self.lives != 0
        except:
            (EnemyDown)


class Player:
    def __init__(self, name, lives):
        self.name = name
        self.lives = lives
        self.score = settings.SCORE
        self.allowed_attacks = settings.ATTACKS

    @staticmethod
    def fight(attack, defense):
        if (attack == 1 and defense == 3) or (attack == 2 and defense == 1) or (attack == 3 and defense == 2):
            return -1
        if (attack == 1 and defense == 1) or (attack == 2 and defense == 2) or (attack == 3 and defense == 3):
            return 0
        if (attack == 1 and defense == 2) or (attack == 2 and defense == 3) or (attack == 3 and defense == 1):
            return 1

    def decrease_lives(self):
        self.lives -= 1
        if self.lives == 0:
            print(f"Your number of scores {self.score}")
            for_write_scores = open("scores.txt", 'a+')
            for_write_scores.write(f"{self.name}: points {self.score}\n")
            for_write_scores.close()
            raise GameOver


    def attack(self, enemy_obj):
        self.allowed_attacks = int(input("Select yuor attack: \n1 - Wizard 2 - Warrior 3 - Robber\n"))
        battle = self.fight(self.allowed_attacks, enemy_obj.select_attack())
        if battle == 0:
            print("It's a draw!\n")
        if battle == 1:
            print("You attacked successfully!\n")
            self.score += 1
            enemy_obj.decrease_lives()
        if battle == -1:
            print("You missed!\n")

    def defence(self, enemy_obj):
        self.allowed_attacks = int(input("Select yuor defence: \n1 - Wizard 2 - Warrior 3 - Robber\n"))
        battle = self.fight(enemy_obj.select_attack(), self.allowed_attacks)
        if battle == 0:
            print("It's a draw!\n")
        if battle == 1:
            print("Enemy attacked successfully!\n")
            self.decrease_lives()
        if battle == -1:
            print("Enemy missed!\n")


