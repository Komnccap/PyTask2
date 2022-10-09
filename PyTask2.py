# Задача №1 - Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
def task1():
    print('Введите число')
    number = float(input())
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
    aray = [num]
    counter = 1
    current_value = 0
    while counter <= num:
        solution = (1+1/counter)**counter
        current_value += solution
        counter += 1
    print(round(current_value, 3))
task3()
# Задача №4 -  Задайте список из N элементов, заполненных числами из промежутка [-N, N].Найдите произведение элементов на позициях a и b.Значения N, a и b вводит пользователь с клавиатуры.
def task4():
    print('Введите Значение N')
    num = int(input())
    nums = []
    counter = -num
    while counter <= num:
        nums.append(counter)
        counter += 1
    print(nums)
    print('Введите позицию первого элемента')
    num2 = int(input())
    num2 -= 1
    print('Введите позицию второго элемента')
    num3 = int(input())
    num3 -= 1
    print('Произвеление равно: ')
    print(nums[num2] * nums[num3])
task4()
# Задача №5 - Реализуйте алгоритм перемешивания списка.
def task5():   
    import random

    number = random.randint(0 , 4)
    value = [1, 2, 3, 4, 5]
    temp = 0
    counter = 0
    print(value, end=' ')
    while counter < 5:
        temp = value[counter]
        value[counter] = value[number]
        value[number] = temp
        counter += 1
    print(value, end=' ')
task5()