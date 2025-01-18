# hw2.py

class Heroes:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def action(self):
        print(f"{self.name} выполняет действие.")

    def attack(self):
        print(f"{self.name} атакует!")

class Archer(Heroes):
    def __init__(self, name, hp, arrows, precision):
        super().__init__(name, hp)
        self.arrows = arrows
        self.precision = precision

    def attack(self):
        if self.arrows > 0:
            self.arrows -= 1
            if self.precision >= 50:
                print(f"{self.name} стреляет! Атака успешна! Стрел осталось: {self.arrows}")
            else:
                print(f"{self.name} стреляет, но промахнулся! Стрел осталось: {self.arrows}")
        else:
            print(f"{self.name} не может атаковать, так как у него нет стрел!")

    def rest(self):
        self.arrows += 5
        print(f"{self.name} отдыхает и восстанавливает 5 стрел. Текущее количество стрел: {self.arrows}")

    def status(self):
        return f"Имя: {self.name}, Здоровье: {self.hp}, Стрел: {self.arrows}, Точность: {self.precision}"

if __name__ == "__main__":
    archer = Archer(name="Лучник", hp=100, arrows=3, precision=60)
    print(archer.status())
    archer.attack()
    archer.rest()
    archer.attack()
    print(archer.status())
