#Задача 1

def task_1 (a: int = 1,
b: float = 1.11,
c: str = 'строка',
d: list = [1, 'Привет', 11] ,
e: bool = True) -> str:
    print (a, 'относится к типу', type(a))
    print (b, 'относится к типу', type(b))
    print (c, 'относится к типу', type(c))
    print (d, 'относится к типу', type(d))
    print (e, 'относится к типу', type(e))
task_1()


#Задача 2

def task_2 (a=[1,2,3,5,8,13,21]) -> int:
    print('a[0:3] =',a[0:3])
task_2()
# Данная последовательность чисел будет являться списком


#Задача 3

def task_3 (number: int):
    return number * number
print(task_3(5))







