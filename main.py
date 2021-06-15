# -*- coding: utf-8 -*-

import random

randomValue = random.randint(0, 100)

print("Введите число от 0 до 100: ")
inputValue = int(input())
print("Случайное число: ", randomValue)

if randomValue < inputValue:
    print("Случайное число меньше")
elif randomValue > inputValue:
    print("Случайное число больше")
else:
    print("Числа равны")