class Hero:
    def __init__(self, name, lvl, HP):
        self.name = name
        self.lvl = lvl
        self.HP = HP

    def introduce(self):
        print(f"Привет, меня зовут {self.name}, мой lvl {self.lvl}, мое HP {self.HP}")

    def is_adult(self):
        return self.lvl >= 10

    def __str__(self):
        return f"Имя: {self.name}, lvl: {self.lvl}, HP: {self.HP}"


hero1 = Hero("Джимбо", 5, 100)
hero2 = Hero("Иванушка", 12, 150)
hero3 = Hero("Ерема", 8, 120)

hero1.introduce()
hero2.introduce()
hero3.introduce()

print(hero1.is_adult())
print(hero2.is_adult())
print(hero3.is_adult())

print(hero1)
print(hero2)
print(hero3)