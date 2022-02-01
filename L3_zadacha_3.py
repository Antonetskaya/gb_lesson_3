# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.



def my_func(a, b, c):
    min_abc = min([a, b, c])
    sum_1 = a + b + c - min_abc
    return sum_1

print(my_func(int(input('Аргумент 1: ')), int(input('Аргумент 2: ')), int(input('Аргумент 3: '))))


