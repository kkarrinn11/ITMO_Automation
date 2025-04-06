# Доп. задание (К дз №4)

class Car:
    def __init__(self, color = None, type = None, year = None):
        self.color = color
        self.type = type
        self.year = year

    def starting_the_car (self):
        print('Автомобиль заведен')

    def turn_off_the_car (self):
        print('Автомобиль заглушен')


    def year_of_car (self, year):
        self.year = year
        print(f'Год выпуска: {self.year}')

    def type_of_car (self, type):
        self.type = type
        print(f'Тип автомобиля: {self.type}')

    def car_color (self, color):
        self.color = color
        print(f'Цвет автомобиля: {self.color}')

car = Car()
car.starting_the_car()
car.year_of_car(2022)
car.type_of_car('Porsche')
car.car_color('Dark green')
car.turn_off_the_car()