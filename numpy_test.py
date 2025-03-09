### Основи роботи з пакетом NumPy

## Створення масивів та матриць в NumPy

import numpy as np
a = np.array([1, 2, 3, 4, 5], dtype=float)
print(a)

m = np.array([[1, 2, 3], [4, 5, 6]], dtype=int)
print(m) 

import numpy as np
a = np.array([1, 2, 3, 4, 5], dtype=float)
print(a.shape)       # (5,)*

m = np.array([[1, 2, 3], [4, 5, 6]], dtype=int)
print(m.shape)  # (2, 3)*

print(m.ndim)
print(m.size)
print(m.dtype)
print(m.data)
print(m.itemsize)


import numpy as np

a = np.ones((5,), dtype=float)
print(a)

m = np.ones((2, 3), dtype=int)
print(m)


import numpy as np

a = np.zeros(5, dtype=float)
print(a)

m = np.zeros((2, 3), dtype=int)
print(m)


m = np.identity(4, dtype=int)
print(m)


import numpy as np

a = np.arange(5)
b = np.arange(1, 3, 0.5)

print(a)
print(b)


import numpy as np

a = np.linspace(1, 5, num=5)
b = np.linspace(1, 3, num=3)

print(a)
print(b)


import numpy as np

a = np.random.random(3)
b = np.random.random((3, 3))

print(a)
print(b)


## Індексація - Масив NumPy можна розділити на частини та присвоїти їм індекси. 
# Принцип роботи схожий на те, як це відбувається зі списками Python.

import numpy as np

a = np.array([1, 2, 3, 4, 5])

print(a[0])
print(a[1:]) # включно з 2-го значення всі значення до кінця рядка 
print(a[:2]) # виключно без 3-го значення всі значення з початку рядка до 3-го значення


a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a)
print(a[0, 0]) # значення у 1-му рядку 1-го стовпчика 
print(a[1, 1]) # значення у 2-му рядку 2-го стовпчика
print(a[2, 1]) # значення у 3-му рядку 2-го стовпчика
print(a[1:, 1]) # починаючи з 2-го рядка включно всі значення у 2-му стовпчику
print(a[0, :2]) # всі значення у 1-му рядку закінчуючи 3-м стовчиком виключно (тільки 1-й, 2-й стовпчик)


## Основні типи даних (dtype) NumPy

import numpy as np

b = np.zeros((3, 3), dtype="u4")
print(b)


import numpy as np

a = np.array([u"\u2211", u"\u220F"], dtype="U")
print(a)  # ['∑' '∏']


## Арифметичні операції

import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)
print(a - b)
print(a * b)
print(a / b)


import numpy as np

a = np.array([
              [1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]
              ])
b = np.array([
              [2, 2, 2],
              [3, 3, 3],
              [4, 4, 4]
              ])

print(a + b)
print(a - b)
print(a * b)
print(a / b)


## Агрегування в NumPy

import numpy as np

a = np.array([1, 2, 3, 4, 5])

print(a.min())
print(a.max())
print(a.sum())
print(a.mean())
print(a.prod())


import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(a.min())
print(a.max())
print(a.sum())
print(a.mean())
print(a.prod())


import numpy as np
q = np.arange(10)  # або q = np.linspace(0,9, num = 10)
print(q)
w = sum(q)
print(w)


## Використання NaN

import numpy as np

# Створення масиву з NaN
arr = np.array([1, 2, np.nan, 4, 5])
print(arr)  # Виведе: [ 1.  2. nan  4.  5.]

# Створення NaN окремо
nan_value = np.nan
print(nan_value)  # Виведе: nan

# Перевірка на NaN
is_nan = np.isnan(arr)
print(is_nan)  # Виведе: [False False  True False False]


# Обчислення середнього значення, ігноруючи NaN
mean_value = np.nanmean(arr)
print(mean_value)  # Виведе: 3.0

# Обчислення суми, ігноруючи NaN
sum_value = np.nansum(arr)
print(sum_value)  # Виведе: 12.0

# Заміна NaN на 0
arr_no_nan = np.nan_to_num(arr)
print(arr_no_nan)  # Виведе: [1. 2. 0. 4. 5.]
print(arr_no_nan.mean())

# Заміна NaN на середнє значення масиву
mean_value = np.nanmean(arr)
arr_no_nan = np.where(np.isnan(arr), mean_value, arr)
print(arr_no_nan)  # Виведе: [1. 2. 3. 4. 5.]


# Масив з відсутніми значеннями
import numpy as np

data = np.array([21, 12, np.nan, 42, 53])

result = np.log(-1)
print(result)  # Виведе: nan

# Обчислення середнього значення, ігноруючи NaN
mean_value = np.nanmean(data)
print(mean_value)  # Виведе: 3.0


## Лінійна алгебра на Python

import numpy as np

a = np.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a)


import numpy as np

a = np.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

diag = np.diag(a)
print(diag)

b = np.diag(diag)
print(b)


import numpy as np

a = np.eye(4, k=0, dtype=float)
print(a)

b = np.eye(4, k=-1, dtype=float)
print(b)

c = np.eye(4, k=-2, dtype=float)
print(c)

d = np.eye(4, k=+1, dtype=float)
print(d)


# Транспонування та зміна форми матриць

import numpy as np

a = np.matrix("1,2,3;4,5,6;7,8,9")
print(a)

b = a.T
print(b)


import numpy as np

a = np.matrix("1,2,3;4,5,6")
print(a)
b = a.reshape((3, 2))
print(b)


import numpy as np

a = np.matrix([[1, 2, 3], [4, 5, 6]])
print(a)
b = a.flatten()
print(b)


## Множення матриць

import numpy as np

a = np.matrix("1,2,3;0,1,2")
b = np.matrix("1,2;0,4;-1,0")
c = a.dot(b)
print(c)


### Внутрішній пакет linalg

## Визначник

import numpy as np

a = np.matrix("1,0,3;-1,-1,2;4,7,2")
det = round(np.linalg.det(a))
print(det)  # -25


## Зворотна матриця

import numpy as np

a = np.matrix("1,0,3;-1,-1,2;4,7,2")
a_inv = np.linalg.inv(a)
print(a_inv)

## Власні значення та власні вектори

import numpy as np

a = np.matrix("1,0,3;-1,-1,2;4,7,2")
w, v = np.linalg.eig(a)
print(w)
print(v)


## Розв'язання систем лінійних рівнянь (різними способами)


# 1) Розв'язання системи лінійних рівнянь у матричній формі

  # Шукаємо матрицю обернену до матриці "a" ("a_inv")
  # і множимо "a_inv" на матрицю "b" знайшовши 3 значення розв'язку рівняння

import numpy as np

a = np.matrix("1,2,5;1,-1,3;3,-6,-1")
b = np.matrix("-9;2;25")
a_inv = np.linalg.inv(a)
x = a_inv.dot(b)
print(x)


# 2) Розв'язання системи лінійних рівнянь методом Крамера
  
  # Підставляємо матрицю "b" у 1-й, 2-й, 3-й стовчик матриці "a"
  # створивши при цьому матриці "a_1", "a_2", "a_3". 
  # Шукаємо визначники (детермінанти) матриць "a_1", "a_2", "a_3" 
  # і ділимо кожен з цих визначників на визначник матриці "a" - знайшовши 3 значення розв'язку рівняння 

import numpy as np

a = np.matrix("1,2,5;1,-1,3;3,-6,-1")
b = np.matrix("-9;2;25")
print(a)
print(b)

a_det = round(np.linalg.det(a))
print(a_det)

a_1 = np.matrix(a)
print(a_1)

a_1[:, 0] = b
print(a_1[:, 0]) # значення всіх рядків для 1-го стовпця матриці "a_1" замінюємо на значення матриці "b"
print(a_1) 

a_2 = np.matrix(a)
a_2[:, 1] = b    # значення всіх рядків для 2-го стовпця матриці "a_1" замінюємо на значення матриці "b"
print(a_2[:, 1]) 
print(a_2)

a_3 = np.matrix(a)
a_3[:, 2] = b    # значення всіх рядків для 3-го стовпця матриці "a_1" замінюємо на значення матриці "b"
print(a_3[:, 2])
print(a_3)

print(round(np.linalg.det(a_1)))
print(round(np.linalg.det(a_2)))
print(round(np.linalg.det(a_3)))

x = [
    round(np.linalg.det(a_1)) / a_det,
    round(np.linalg.det(a_2)) / a_det,
    round(np.linalg.det(a_3)) / a_det,
]
print(x)


### Домашня робота NumPy

## Перше завдання
# Вкладник поклав 50000 умовних одиниць на три різні рахунки 
# в три різні банки. 
# За першим рахунком виплати становитимуть 5% річних, 
# по другому – 7% річних та по третьому 6% річних. 
# Відомо, що через рік вкладник отримав за відсотками 
# суму в 2250 у.о. з першого та другого банку та 
# суму в 1400 у.о. з першого та третього банку. 
# Скільки умовних одиниць він поклав на кожен рахунок спочатку?

# x1 + x2 + x3 = 50000
# 0,05x1 + 0,07x2 = 2250
# 0,05x1 + 0,06x3 = 1400

import numpy as np
a = np.matrix("1,1,1;  0.05, 00.7, 0;  0.05, 0, 0.06")
print(a)

a_inv = np.linalg.inv(a)
print(a_inv)

b = np.matrix("50000; 2250; 1400")
print(b)

x = np.linalg.solve(a_inv,b)
print(x)



