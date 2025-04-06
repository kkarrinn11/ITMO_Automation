# Задача 1

class Rectangle:

    def __init__ (self, width, height):
        self.width = width
        self.height = height

    def calculate_area (self):
        return self.width * self.height

    def calculate_perimeter (self):
        return 2 * (self.width + self.height)


rectangle1 = Rectangle (5, 7)
rectangle2 = Rectangle (12, 6)
rectangle3 = Rectangle (42, 16)

print(f'Прямоугольник 1: Площадь = {rectangle1.calculate_area()}, Периметр = {rectangle1.calculate_perimeter()}')
print(f'Прямоугольник 2: Площадь = {rectangle2.calculate_area()}, Периметр = {rectangle2.calculate_perimeter()}')
print(f'Прямоугольник 3: Площадь = {rectangle3.calculate_area()}, Периметр = {rectangle3.calculate_perimeter()}')



# Задача 2

class Math:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition (self):
        return self.a + self.b

    def multiplication (self):
        return self.a * self.b

    def division (self):
        if self.b != 0:
            return self.a / self.b
        else:
            print('Делить на ноль нельзя')

    def subtraction (self):
        return self.a - self.b

attribute = Math (2, 5)

print('Сложение', attribute.addition())
print('Умножение', attribute.multiplication())
print('Деление', attribute.division())
print('Вычитание', attribute.subtraction())



# Задача 3

class Button:
    def __init__(self, text, locator = ''):
        self.text = text
        self.type = 'Кнопка'
        self.locator = locator

    def click (self):
        return f'Клик по кнопке {self.text}'

    def __str__ (self):
        return f'Текст: {self.text}, Тип: {self.type}, Локатор: {self.locator}'


text_box_button = Button ("Text Box")
check_box_button = Button ("Check Box")
radio_button_button = Button ("Radio Button")
web_tables_button = Button ("Web Tables")
buttons_button = Button ("Buttons")
links_button = Button ("Links")
broken_links_button = Button ("Broken Links - Images")
upload_download_button = Button ("Upload and Download")
dynamic_properties_button = Button ("Dynamic Properties")


buttons = [
    text_box_button,
    check_box_button,
    radio_button_button,
    web_tables_button,
    buttons_button,
    links_button,
    broken_links_button,
    upload_download_button,
    dynamic_properties_button
]

print('Информация о кнопках:')
for button in buttons:
    print(button)

print('\nКлики по кнопкам:')
for button in buttons:
    print(button.click())

