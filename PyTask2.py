# Задача №1 - Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
def task1():
    print('Введите число')
    number = int(input())
    sum = 0
    print("Сумма цифр числа равна:")
    while number > 0:
        solution = number % 10
        if solution != 0:
            sum += solution
            number = number // 10
    print(sum)
task1()
# Задача №2 - Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
def task2():    
    print('Введите число')
    number = int(input())
    counter = 1
    currentSum = 1
    print("Набор произведений равен")
    while counter <= number:
        currentSum *= counter
        counter += 1
        print(currentSum)
task2()
# Задача №3 - Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму, округлённую до трёх знаков после точки.
def task3():
    print('Введите число')
    num = int(input())
    solution = (1+1/num)**num
    solution2 = round(solution, 3)
    print(solution2)
task3()
# Задача №4 -  Задайте список из N элементов, заполненных числами из промежутка [-N, N].Найдите произведение элементов на позициях a и b.Значения N, a и b вводит пользователь с клавиатуры.
def task4():
    print('Введите Значение N')
    num = int(input())
    numbers = [-num, num]
    counter = -num
    while counter <= num:
        print(counter, end=' ')
        counter += 1
    print(numbers)
    print('Введите первое число')
    num2 = int(input())
    print('Введите второе число')
    num3 = int(input())
    print(num2 + num3)
task4()
# Задача №5 - Реализуйте алгоритм перемешивания списка.
def task5():
    import random

    value = ['лучше', 'иметь', 'и', 'не', 'нуждаться', 'чем', 'нуждаться', 'и', 'не', 'иметь']
    random.shuffle(value)
    print(value, end=' ')
task5()