############# Тема 4. Регулярні вирази та розширена робота з рядками


# this_is_string = "Hi there!"
# the_same_string = 'Hi there!'
# this_is_string == the_same_string # True

# print(this_is_string)
# print(this_is_string == the_same_string)


# text = """This is first line
# And second line
# Last third line"""

# song = '''Jingle bells, jingle bells
# Jingle all the way
# Oh, what fun it is to ride
# In a one horse open sleigh'''

# print(text)
# print(song)



# one_line_text = "Textual data in Python is handled with str objects, or strings. Strings are immutable sequences of Unicode code points. String literals are written in a variety of ways: single quotes, double quotes, triple quoted."
# print(one_line_text)


# one_line_text = "Textual data in Python is handled with str objects," \
#                 " or strings. Strings are immutable sequences of Unicode" \
#                 " code points. String literals are written in a variety " \
#                 " of ways: single quotes, double quotes, triple quoted."
# print(one_line_text)


# ("spam " "eggs") == "spam eggs"  # True
# print(("spam " "eggs") == "spam eggs")

# a = "spam " + "eggs"
# b = "spam " "eggs"
# print(a==b)
# print(a)
# print(b)


# one_line_text = ("Textual data in Python is handled with str objects,"
#                 " or strings. Strings are immutable sequences of Unicode"
#                 " code points. String literals are written in a variety "
#                 " of ways: single quotes, double quotes, triple quoted.")
# print(one_line_text)


# query = ("SELECT * "
#          "FROM some_table "
#          "WHERE condition1 = True "
#          "AND condition2 = False")


# print("Hello\nWorld")
# print("Hello\tWorld")

# print("Hello my little\rsister")

# print("my little\rsister")


# print("Hello\bWorld")
# print("Hello\b World")

# print("Hello\\World")

# print('It\'s a beautiful day')
# print("He said, \"Hello\"")




# s = "Hi there!"

# start = 0
# end = 7

# print(s.find("er", start, end)) # 5
# print(s.find("q")) # -1



# s = 'Some words'

# print(s.find("o"))
# print(s.rfind('o'))


# s = 'Some words'

# print(s.index("o"))
# print(s.rindex('o'))


# str.split(separator=None, maxsplit=-1)

# text = "hello world"
# result = text.split()
# print(result)  # Виведе: ['hello', 'world']


# text = "apple,banana,cherry"
# result = text.split(',')
# print(result)  # Виведе: ['apple', 'banana', 'cherry']


# string.join(iterable)

# list_of_strings = ['Hello', 'world']
# result = ' '.join(list_of_strings)
# print(result)  # Виведе: 'Hello world'


# elements = ['earth', 'air', 'fire', 'water']
# result = ', '.join(elements)
# print(result)  # Виведе: 'earth, air, fire, water'


# print('TestHook'.removeprefix('Test')) # Hook
# print('TestHook'.removeprefix('Hook')) # TestHook

# print('TestHook'.removesuffix('Test'))
# print('TestHook'.removesuffix('Hook'))

# url_search = "<https://www.google.com/search?q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t>"
# _, query = url_search.split('?')
# print(_)
# print(query)


# url_search = "<https://www.google.com/search?q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t>"
# _, query = url_search.split('?')
# print(query)

# obj_query = {}
# for el in query.split('&'):
#     key, value = el.split('=')
#     obj_query.update({key: value.replace('+', ' ')})
# print(obj_query)



# number = "12345"
# print(number.isdigit())  # Виведе: True

# text = "Number123"
# print(text.isdigit())  # Виведе: False


# user_input = input("Введіть число: ")
# if user_input.isdigit():
#     print("Це дійсно число!")
# else:
#     print("Це не число!")

# for char in "Hello 123":
#     if char.isdigit():
#         print(f"'{char}' - це цифра")
#     else:
#         print(f"'{char}' - не цифра")




# intab = "aeiou"
# outtab = "12345"
# trantab = str.maketrans(intab, outtab)

# print(trantab)

# str = "This is string example"
# print(str.translate(trantab))




# intab = "aeiou"
# trantab = str.maketrans('', '', intab)

# str = "This is string example"
# print(str.translate(trantab))


# intab = "aeiou"
# trantab = str.maketrans('', '', intab)

# print(trantab)

# str = "This is string example"
# print(str.translate(trantab))




# symbols = "0123456789ABCDEF"
# code = [
#         '0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111',
#         '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111'
#         ]

# MAP = {}

# for s, c in zip(symbols, code):
#     MAP[ord(s)] = c
#     MAP[ord(s.lower())] = c

# result = "34 DF 56 AC".translate(MAP)
# print(result)




# morze_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
#               'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
#               'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
#               'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
#               'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
#               '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
#               '8': '---..', '9': '----.'}

# # Перетворення ключів словника на Unicode коди
# table_morze_dict = {}
# for k, v in morze_dict.items():
#     table_morze_dict[ord(k)] = v

# string = "Hello world"

# result = ""

# for ch in string:
#     result = result + ch.upper().translate(table_morze_dict)

# print(result)



# width = 5
# for num in range(12):
#     print(f'{num:^10} {num**2:^10} {num**3:^10}')


# name = "Alice"
# formatted = f"{name:>10}"
# print(formatted)  # Виведе: '     Alice' (вирівнювання праворуч)


# name = "Alice"
# formatted = f"{name:^10}"
# print(formatted)  # Виведе: '     Alice' (вирівнювання праворуч)


# completion = 0.756
# formatted = f"{completion:.1%}"
# print(formatted)  # Виведе: '75.6%'
# print(type(formatted))



# import re

# # re.search(pattern, string)

# import re

# text = "Вивчення Python може бути веселим."
# pattern = "Python"
# match = re.search(pattern, text)
# print(match)


# if match:
#     print("Знайдено:", match.span())
# else:
#     print("Не знайдено.")


# if match:
#     print("Знайдено:", match.string)
# else:
#     print("Не знайдено.")


# if match:
#     print("Знайдено:", match.group())
# else:
#     print("Не знайдено.")



# import re

# text = "Моя електронна адреса: example@example.com"
# pattern = r"\w+@\w+\.\w+"
# match = re.search(pattern, text)

# if match:
#     print("Електронна адреса:", match.group())



# import re

# email = "username@domain.com"
# pattern = r"(\w+)@(\w+\.\w+)"
# match = re.search(pattern, email)

# if match:
#     user_name = match.group(1)
#     domain_name = match.group(2)
#     print("Ім'я користувача:", user_name)
#     print("Домен:", domain_name)



# import re

# text = "Рік 2023 був складнішим, ніж 2022"
# pattern = r"\d+"
# matches = re.findall(pattern, text)

# print(matches)



# import re

# text = "Контакти: example1@example.com, example2@sample.org"
# pattern = r"\w+@\w+\.\w+"
# matches = re.findall(pattern, text)

# print(matches)  # Виведе всі знайдені електронні адреси



# import re

# file_name = "Мій документ Python.txt"
# pattern = r"\s"
# replacement = "_"
# formatted_name = re.sub(pattern, replacement, file_name)

# print(formatted_name)  



# import re

# text = "Python - потужна, універсальна; мова!"
# pattern = r"[;,\-:!\.]"
# replacement = ""
# modified_text = re.sub(pattern, replacement, text)

# print(modified_text)



# import re

# phone = """
#         Михайло Куліш: 050-171-1634
#         Вікторія Кущ: 063-134-1729
#         Оксана Гавриленко: 068-234-5612
#         """
# pattern = r"(\d{3})-(\d{3})-(\d{4})"
# replacement = r"(\1) \2-\3"
# formatted_phone = re.sub(pattern, replacement, phone)

# print(formatted_phone)



# import re

# text = "Python - це проста, але потужна мова програмування."
# pattern = r"\s+"
# words = re.split(pattern, text)

# print(words)  # Виведе список слів у рядку


# import re

# text = "Python - потужна; проста, універсальна: мова!"
# pattern = r"[;,\-:!\s]+"
# elements = re.split(pattern, text)

# print(elements)  # Виведе список частин, розділених пунктуацією


import re

text = "apple#banana!mango@orange;kiwi"
pattern = r"[#@;!]"
fruits = re.split(pattern, text)

print(fruits)




































######### Лекція 4. чт 06.03.2025. Тема 4. Регулярні вирази та розширена робота з рядками (лектор Сергій Коденко)

s1 = 'Hello World'
s2 = 'Hello Python'
text1 = '''Helloo world 
        and Python'''       # виводить як 2 різні рядки

'''
Коментар
Багаторядковий
Хоч він і не зовсім коментар
'''

# text2 = 'very long tex is here'\ 
#         'to show how it works'    # виводить як 1 рядок

# print(s1,s2,text1,text2, sep="\n")


# a = 3
# a = a +\
# 3

# text2 = 'very long tex is here \n to show how it works'  
# print(text2)

# text3 = '\t1\t2\t20\t100\n100\t20\t1\t2'
# print(text3, sep='\n')


# text2 = 'very long tex is here \r to show how it works'  
# print(text2, sep='\n')

# import time
# for i in range(100):
#     print(f"\r{i}% Ready", end='')  # \r повертає на початок рядка
#     time.sleep(.1)
# print(text2, sep='\n')


# print("very long text", end='') # end='' не переносить на новий рядок
# print("\rshort text")


# text4 = 'text pt 1\vtext pt 2'   # вертикальна табуляція на Windows не працює
# print(text4)

# text4 = 'text pt 1 \f\f\f text pt 2'   # вертикальна табуляція на Windows не працює
# print(text4)

# text4 = 'text pt 1 \n\t text pt 2'   # майже аналог вертикальної табуляція на Windows
# print(text4)

# text4 = 'text pt 1 \b\b\b text pt 2'   # backspace
# print(text4)


# print('\'')       # \ екранує знак ' лапок
# print('\'    \\')
# print('\'    \\   \077')
# print('\'    \\   \xc3')


### функції рядків

s = 'Hello shiny wolrd!'
# print(s.find("l"))
# print(s.find("o"))
# print(s.find("shiny"))
# print(s.find("x"))

# print(s.rfind("l"))   # right find з кінця шукає й нумерація з кінця символів йде
# print(s.count("l"))

#                       # знайти 2-гу 'l'

# start = s.find('l')+1          # шукаємо 1-шу "l" + 1 позиція
# print(s.find('l', start))      # 2-гу "l" починаючи з +1 позиції від 1-ї "l"



# s = 'Hello shiny wolrd!'

# print(s.index('l'))

# # print(s.index('x')) # видає Value Error, якшр такого символа немає в рядку
# print(s.find("x")) # повертає не помилку, а -1


# try:
#     print(s.index('l'))
# except Exception as e:
#     print(e)


# try:
#     print(s.rindex('l', 5))  # починаємо шукати з 5-го символу
# except Exception as e:
#     print(e)


# try:
#     print(s.rindex('с', 5))
# except Exception as e:
#     print("Not Found")



#### метод split()

# s = 'Hello shiny wolrd!'

# print(s.split(' '))

# print(s.split('l'))


# input = 'Snitch John j.snitch@gmail.com +123456789'
# print(input.split("it"))

# l1 = input.split()

# csv_line = ','.join(l1)   # comma-separated value
# print(csv_line)




##### вставити код по csv  input2  !!!!!

# !!!!




# s = '   some nice text   '
# l1 = ['John    ', ' Smith  ', '    coolmail@mail.com', '+657677766  ']
# l2 = []
# print('|', end='')
# print(s.strip(), end='')  # прибирає зайві пробіли на початку та в кінці
# print('|')
# for el in l1:
#     l2.append(el.strip())
# print(l2)

# for el in l1:
#     l2.append(el.rstrip())
# print(l2)




# s = '   some nice text   '.strip()
# print(s)

# print(s.replace('nice', 'cool'))



# s = '   some nice text nice nice  '.strip()
# # print(s)

# print(s.replace('nice', 'cool'))



# s = '   some nice text nice nice  '.strip()
# print(s)

# s = s.replace('nice', 'cool', 1)   # бо рядкі незмінні, тому треба створювати нову змінну
# print(s.replace('nice', 'cool', 1)) # заміна тільки 1-шого 'nice' на 'cool'


# print(s.replace(' ', ''))


# s3 = 'cool'.join(s.split('nice'))
# print(s3)



##### видалення суфіксів (постфікси) і префіксів


# s = 'some nice text'
# s1 = 'cool nice text'
# s2 = 'some nice texts'
# print(s.removeprefix('some'))    # прибрати слово some на початку, якщо рядок починається з цього префікса
# print(s1.removeprefix('some'))
# print(s2.removeprefix('some'))

# print(s.removesuffix('text'))    # прибрати слово some на початку, якщо рядок починається з цього префікса
# print(s1.removesuffix('text'))
# print(s2.removesuffix('text'))


# l = ['1', '2', 'n=2', 'n=3']
# for el in l:
#     print(el.removeprefix('n='))

# orig = 'somenictxl'
# trans= 'соменіцтхл'
# s = 'some nice text'
# s1 = 'cool nice text'
# s2 = 'some nice texts'

# trans_tab = str.maketrans(orig, trans)  # табличка транслітерації англ букв в укр букви
# print(s.translate(trans_tab))  # виведення проведеної транслітерації на основі табличка транслітерації.




##### форматування рядків  f-string

# for i in range(8):
#      print(f'int: {i:d}; hex{i:#x}; '\
#      f'oct:{i:#o}; bin:{i:#b}; float:{i:f}')



# for i in range(8):
#      print(f'int: {i:d}; hex{i:#4x}; '\
#      f'oct:{i:#5o}; bin:{i:#7b}; float:{i:4.1f}')


# for i in range(8):
#      print(f'int: {i:d}; hex{i:#4x}; '\
#      f'oct:{i:#5o}; bin:{i:<7b}; float:{i:4.1f}')


# for i in range(8):
#      print(f'int: {i:d}; hex{i:#4x}; '\
#      f'oct:{i:#5o}; bin:{i:^#7b}; float:{i:4.1f}')



# ###### Регулярні вирази (Regular expressions) re - regex, regexp
# # описуємо рядки за допомогою умонвих позначок

# import re 

# # re.findall()

# s = '1234 asd1234 1234 sadas 1231 123 123 asd'
# pat1 = r'[0-9]{1,}'  # r'[0-9 a-z]'   r'[01234456789]'   {1,} від 1 і більше разів має зустрічатися число
#                      # raw string
# res1= re.findall(pat1, s)    # знайти всі входження - дуже часто використовується
# print(res1)

# s = '1234 asd1234 1234 sadas 1231 123 123 asd'
# pat1 = r'[0-9]{1,3}'  # r'[0-9 a-z]'   r'[01234456789]'   {1,3} від 1 і до 3 разів має зустрічатися число - розбивається на шматочки по 3 символи
#                      # raw string
# res1= re.findall(pat1, s)    # знайти всі входження - дуже часто використовується
# print(res1)


# s = '1234 asd1234 1234 sadas 1231 123 123 asd'
# pat1 = r'[a-zA-Z]{1,3}'  # r'[0-9 a-z]'   r'[01234456789]'   {1,3} від 1 і до 3 разів має зустрічатися число
#                      # raw string
# res1= re.findall(pat1, s)    # знайти всі входження - дуже часто використовується
# print(res1)

# # d - digit
# # +  1 і більше


# s = '1234 asd1234 1234 sadas 1231 123 123 asd'
# pat1 = r'\d{1,3}'  # r'[0-9 a-z]'   r'[01234456789]'   {1,3} від 1 і до 3 разів має зустрічатися число - розбивається на шматочки по 3 символи
#                      # raw string
# res1= re.findall(pat1, s)    # знайти всі входження - дуже часто використовується
# print(res1)

# s = '1234+asd1234 +1234 sadas+ 1231 123+ 123 asd'
# pat1 = r'\d+'  # r'[0-9 a-z]'   r'[01234456789]'   {1,3} від 1 і до 3 разів має зустрічатися число - розбивається на шматочки по 3 символи
#                      # raw string
# res1= re.findall(pat1, s)    # знайти всі входження - дуже часто використовується
# print(res1)


# s = '1234+asd1234 +1234 sadas+ 1231 123+ 123 asd'
# pat1 = r'\d+'  # r'[0-9 a-z]'   r'[01234456789]'   {1,3} від 1 і до 3 разів має зустрічатися число - розбивається на шматочки по 3 символи
#                      # raw string
# res1= re.findall(pat1, s)    # знайти всі входження - дуже часто використовується
# print(res1)

# s = '1234+asd1234 +1234 sadas+ 1231 123+ 123 asd'
# pat1 = r'\++'  # r'[0-9 a-z]'   r'[01234456789]'   {1,3} від 1 і до 3 разів має зустрічатися число - розбивається на шматочки по 3 символи
#                      # raw string
# res1= re.findall(pat1, s)    # знайти всі входження - дуже часто використовується
# print(res1)




# # re.search()   # видає єдине входження яке відповідає патерну, індекси
# s = '1234+asd1234 +1234 sadas+ 1231 123+ 123 asd'
# pat1 = r'\++'  # r'[0-9 a-z]'   r'[01234456789]'   {1,3} від 1 і до 3 разів має зустрічатися число - розбивається на шматочки по 3 символи
#                      # raw string
# res1= re.findall(pat1, s)    # знайти всі входження - дуже часто використовується
# print(res1)
# res2=re.search(pat1, s)
# print(res2)




import re

# s2 = 'pi is 3.14 and it\'s a constant'   # \' апостроф, не лапки
# pat2 = r'\d\.\d+'
# print(re.findall(pat2, s2))

# import re

# s2 = 'pi is 3.14 and it\'s a constant, .5 is also a constant but has no name'
# pat2 = r'\d*\.\d+'
# print(re.findall(pat2, s2))


# mail = 'jsmith@mai.com'  # перевірка і-мейлів що є а що не є імейлом
# pat3 = r'w+@\w+\.\w'
# print(re.match(pat3, mail))   # перевіряючи рядок від початку співпадає з палітрою
# print(re.match(pat3, mail).group()) 




# ##### взяти з кода від лектора !!!!!!!
# re.findall()
# pat3 = r'^[w+@\w+\.\w]'   # ^ початок рядка











# # pat3=r'[\w\._]+@\w+\.\w+'
# прикласти cheat sheet
import re #regular expressions regex regexp

# s='1234+78998 7+++asd1234  ++ ++ 1234sdas 1231 123 123asdasd'
# pat1=r'\w+'
# # d - digit
# # + - 1 і більше
# res1=re.findall(pat1,s)
# res2=re.search(pat1,s)
# print(res1)
# print(res2.group())
# print(res2.span())
# s2='pi is 3.14 and it\'s a constant'\
#     ', .5 is also a constant but has no name'

# pat2=r'\d*\.\d+'
# print(re.findall(pat2,s2))

# mail="j.s_m_ith@stud.mail.com '; drop database; coll_11@10mituesmail.com
