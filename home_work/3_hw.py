# Задача 1
def hw_1 (a, b):
    if a > b:
        return a
    else:
        return b

print (hw_1(1, 2))



# Задача 2
def hw_2 (a, b):
    if abs(a - b) == 135:
        return ('yes')
    else:
        return ('no')

print(hw_2(100, 235))



# Задача 3
def the_seasons (month_number):
     if month_number == 12 or month_number == 1 or month_number == 2 :
         print('Зима')
     elif month_number in range (3, 6):
        print('Весна')
     elif 6 <= month_number <= 8:
         print('Лето')
     elif 9 <= month_number <= 11:
         print('Осень')
     else:
        print('Введите корректное название месяца')

the_seasons (13)



# Задача 4
def hw_4 (a, b, c):
    if a > 10 and b > 10 and c > 10:
        return ('yes')
    else:
        return ('no')

print(hw_4(11, 12, 13))



# Задача 5
numbers = (-1, 23, 17, 0, -14)
def positive (numbers):
    count = sum(1 for num in numbers if num > 0)
    return count

print(positive(numbers))



# Задача 6
def count_days (years, months):
    days_in_years = years * 12 * 29
    days_in_months = months * 29
    total_days = days_in_years + days_in_months
    print(total_days)

count_days(2, 7)