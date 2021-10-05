print("Hello!")
print("Dear!")

# Объявление переменных
value = 10.1
student_Name = "AleXXXey"

age1 = 22
str_1 = 'I love MPEI'
str_2 = "по субботам"
# Их реализация
print(str_1 + ' ' + str_2 + ' ' + str(value) + ' раз')

sum1 = value < age1
print (sum1)

# Создаем список
s=list()
s1 = [1, 2]
s1.append(3)

s2 = s1[2]
print(s1, s2)

#Создаем кортеж
s3 = tuple()
s3 = (1,2, 3, 4)
print (s3)

#Создание словаря
d = dict()
d = {2: 'Semen', 1: 'Vasya'}

sss = True
if (value < age1):
    print ("Ты лох")
elif sss:
    print (sss)

#Цикл while
t = True
i = 0
while t:
    print ("a")
    i += 1
    if i >= 10:
        t = False
        print (i)
print ('---')

j = 0
while j < 10:
    print (j)
    j += 1
print ('---')
#Цикл for
for k in range (10, 5, 1):
    print (k)

#Проходимся по списку
s1 =["M", "P", "E", "I"]

for i in s1:
    print (i)

#break

for letter in "лучший":
    if letter == "ш":
        continue
    elif letter == "й":
        break
    print (letter)

#def
def yotx(arg1):
    out = 3* arg1
    return out
print(yotx(5))
print ('-----')

def yotx(*args):
    for argument in args:
        print (argument)

yotx (1, 'a', True)
print("---")

#import
import math as m
import main
from math import sqrt as s

main.print_hi()
m.pi
s()



def graph (num, title, y, x):
    pyplot.subplot(2, 2, num)
    pyplot.grid(True)
    if title == 'Переходная характеристика':
        pyplot.plot(x, y, 'purple')
    elif title == 'Импульсная характеристика':
        pyplot.plot(x, y, 'green')
    pyplot.title(title)
    pyplot.ylabel('Амплитуда')
    pyplot.xlabel('Время (с)')

unitName = choice()
unit = getUnit(unitName)

timeLine = []
for i in range(0, 10000):
    timeLine.append(i/1000)

omega = []
for i in range(0, 1000):
    omega.append(i/1000)

[y,x] = matlab.step(unit, timeLine) #переходная функция
graph(1, 'Переходная характеристика', y, x)

[y,x] = matlab.impulse(unit, timeLine) #импульсная функция
graph(3, 'Импульсная характеристика', y, x)


mag, phase, omega = matlab.freqresp(unit, omega)
pyplot.subplot(2, 2, 2)
pyplot.plot(omega, mag)
pyplot.grid(True)
pyplot.subplot(2, 2, 4)
pyplot.plot(omega, phase * 180 / math.pi)
pyplot.grid(True)
pyplot.show()
