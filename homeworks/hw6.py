# hw6.py

# Базовый класс Robot
class Robot:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Привет, я робот {self.name}.")


# Базовый класс Machine
class Machine:
    def __init__(self, model):
        self.model = model

    def show_model(self):
        print(f"Моя модель: {self.model}")


# Класс с множественным наследованием
class RoboMachine(Robot, Machine):
    def __init__(self, name, model):
        # Инициализируем оба родительских класса
        Robot.__init__(self, name)
        Machine.__init__(self, model)

    # Дополнительный метод для демонстрации функционала
    def perform_task(self, task):
        print(f"{self.name} выполняет задачу: {task}.")


# Пример использования
robo1 = RoboMachine("RoboX", "RX-2000")
robo1.greet()  # Привет, я робот RoboX.
robo1.show_model()  # Моя модель: RX-2000
robo1.perform_task("сборка деталей")  # RoboX выполняет задачу: сборка деталей.
