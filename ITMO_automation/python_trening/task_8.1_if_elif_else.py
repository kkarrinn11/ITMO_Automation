from queue import PriorityQueue

num_float = 3.4

# Также попробовать варианты
# num_float = 0
# num_float = -4.5

# if num_float > 0:
#     print('Положительное число')
# elif num_float == 0:
#     print('Ноль')
# else:
#     print('Число отрицательное')


# permit_print = True
#
# if num > 0 and permit_print:
#     print ('num - положительное число')
# elif not permit_print:
#     print('Печать запрещена')



# def student_rank (year_of_study):
#     if year_of_study == 1 or year_of_study == 2 or year_of_study == 3 or year_of_study == 4:
#         print('Вы - бакалавр')
#     elif year_of_study in range (5, 7):
#         print('Вы - магистр')
#     elif 7 <= year_of_study <= 9:
#         print('Вы - аспирант')
#     else:
#         print('Введите корректный год обучения')
#
# student_rank(8)


a = 101
if a > 100 or a < -100:
    print('-')
else:
    print('+')