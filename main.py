from abc import ABC, abstractmethod
import random

class Hero(ABC):
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.__random_int = random.randint(1, 3)

    def attack(self):
        print(f"{self.name} атакует!")

    def protection(self):
        print(f"{self.name} защищается!")

    def rest(self):
        print(f"{self.name} отдыхает!")

    def get_random_int(self):
        return self.__random_int

    @abstractmethod
    def unique_attack(self):
        pass

    @abstractmethod
    def unique_scream(self):
        pass

    @abstractmethod
    def action(self):
        random_action = self.get_random_int()
        if random_action == 1:
            self.attack()
        elif random_action == 2:
            self.protection()
        elif random_action == 3:
            self.rest()

class Jester(Hero):
    def unique_attack(self):
        print(f"{self.name} использует уникальную атаку — 'Клоунский шут'!")

    def unique_scream(self):
        print(f"{self.name} издает громкий крик — 'Йо-хо-хо!'")

    def action(self):
        super().action()
        print(f"{self.name} выполняет свою уникальную реакцию.")
        self.unique_attack()
        self.unique_scream()