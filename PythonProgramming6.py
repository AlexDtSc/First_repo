############### Тема 6. Робота з модулями та створення віртуального оточенн

# import math

# sin_pi = math.sin(math.pi)
# print(sin_pi)


# from math import pi, sin

# sin_pi = sin(pi)
# print(sin_pi)



# main.py
# import mymodule

# print(mymodule.say_hello("World"))



# main.py
# from mymodule import say_hello

# print(say_hello("World"))



# main.py
# from mymodule import say_hello as greeting

# print(greeting("World"))


# from module_name import item_name as alias



# main.py
# from mymodule import say_hello as greeting

# print(dir())
# print(greeting("World"))


# from mymodule import say_hello

# print(dir())
# print(say_hello("World"))


# import mymodule

# print(dir())
# print(mymodule.say_hello("World"))



# # main.py
# from mymodule import say_hello as greeting

# print(greeting("World"))




import sys
import os


# print(sys.modules["os"])

import sys
import os

# print(sys.modules.keys())

import sys
import os

# print(sys.builtin_module_names)


# import sys
# print(sys.path)

import sys

for arg in sys.argv:
    print(arg)



# from pathlib import Path
# directory = Path('./calculations')
# directory.mkdir(parents=True, exist_ok=True)




# from calculations import salary_calculations

# salary = 1000
# bonus = 15
# salary_with_bonus = salary_calculations.add_bonus(salary, bonus)
# print(salary_with_bonus)  # 1015



# from calculations.salary_calculations import add_bonus

# salary = 1000
# bonus = 15
# salary_with_bonus = add_bonus(salary, bonus)
# print(salary_with_bonus)  # 1015



# from pathlib import Path
# directory = Path('./utility/useful')
# directory.mkdir(parents=True, exist_ok=True)

# directory = Path('./utility/dummy')
# directory.mkdir(parents=True, exist_ok=True)


# from pathlib import Path

# path = Path("./utility/useful/functions.py")

# # Перевірка існування
# if path.exists():
#     print(f"{path} існує")



# import utility

# utility.useful.functions.nice_function()
# utility.dummy.functions.not_bad("Test string")



# import utility.useful.functions, utility.dummy.functions 

# print(utility.useful.functions.nice_function())
# print(utility.dummy.functions.not_bad("Test string"))


# from utility import nice_function, not_bad

# nice_function()
# not_bad("Test string")

# from utility import *

# nice_function()
# not_bad("Test string")



# print("It's OK")



#### venv
# from colorama import Fore, Back, Style

# print(Fore.RED + 'Це червоний текст')
# print(Back.GREEN + 'Це текст на зеленому фоні')
# print(Style.RESET_ALL)
# print('Це звичайний текст після скидання стилю')



# def is_even(number: int) -> bool:
#     if number % 2 == 0:
#         return True
#     else:
#         return False

# print(is_even(4))
# print(is_even(3))



# def is_even(number: int) -> bool:
#     return number % 2 == 0

# print(is_even(4))
# print(is_even(3))




# def is_palindrome(s: str) -> bool:
#     new_s = ""
#     for char in s:
#         if char.isalnum():
#             new_s += char.lower()
#     s = new_s
#     length = len(s)
#     for i in range(length // 2):
#         if s[i] != s[length - i - 1]:
#             return False
#     return True

# # Використання функції
# print(is_palindrome("Козак з казок"))  # Виведе: True
# print(is_palindrome("Миша з нори"))    # Виведе: False



# def is_palindrome(s: str) -> bool:
#     new_s = ""
#     for char in s:
#         if char.isalnum():
#             new_s += char.lower()

#     s = new_s
#     return s == s[::-1]

# # Використання функції
# print(is_palindrome("Козак з казок"))  # Виведе: True
# print(is_palindrome("Миша з нори"))    # Виведе: False


# # Розрахунок площі 
# length1, width1 = 5, 10
# area1 = length1 * width1

# # Багато різного коду

# length2, width2 = 7, 12
# area2 = length2 * width2


# def calculate_area(length: float, width: float) -> float:
#     return length * width

# area1 = calculate_area(5, 10)
# area2 = calculate_area(7, 12)



# from math_operations import calculate_area

# area1 = calculate_area(10, 5)
# area2 = calculate_area(20, 15)




###### Практика з викладачем 16.03.2025