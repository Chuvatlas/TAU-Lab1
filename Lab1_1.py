import matplotlib.pyplot as pyplot
import control.matlab as matlab
import numpy as numpy
import math
import colorama as color

def choice():
    inertialessUnitName = 'Безынерционное звено'
    aperiodicUnitName = 'Апериодическое звено'
    integrateUnitName = 'Интегрирующее звено'
    idealDifferentiativeUnitName = 'Идеальное дифференцирующее звено'
    realDifferentiativeUnitName = 'Реальное дифференцирующее звено'
    needNewChoice = True

    while needNewChoice:
        userInput = input('Введите номер команды: \n'
                           '1 - ' + inertialessUnitName + ';\n'
                           '2 - ' + aperiodicUnitName + ';\n'
                           '3 - ' + integrateUnitName + ';\n'
                           '4 - ' + idealDifferentiativeUnitName + ';\n'
                           '5 - ' + realDifferentiativeUnitName + '.\n')
        if userInput.isdigit():
            needNewChoice = False
            userInput = int(userInput)
            if userInput == 1:
                name = 'Безынерционное звено'
            elif userInput == 2:
                name = 'Апериодическое звено'
            elif userInput == 3:
                name = 'Интегрирующее звено'
            elif userInput == 4:
                name = 'Идеальное дифференцирующее звено'
            elif userInput == 5:
                name = 'Реальное дифференцирующее звено'
            else:
                print(color.Fore.RED + '\nНедопустимое числовое значение!')
                needNewChoice = True

        else:
            print(color.Fore.RED + '\nПожалуйста, введите числовое значение!')
            needNewChoice = True
    return name

#Мат. описание звена по его имени
def getUnit(name):
    needNewChoice = True
    while needNewChoice:
        print(color.Style.RESET_ALL)
        needNewChoice = False
        k = input('Пожалуйста, введите значение коэффициента k = ')
        t = input('Пожалуйста, введите значение коэффициента t = ')
        if k.isdigit() and t.isdigit():
            k = int(k)
            t = int(t)
            if name == 'Безынерционное звено':
                unit = matlab.tf([k], [1])
            elif name == 'Апериодическое звено':
                unit = matlab.tf([k], [t, 1])
            elif name == 'Интегрирующее звено':
                unit = matlab.tf([k], [1, 0])
            elif name == 'Идеальное дифференцирующее звено':
                unit = matlab.tf([k, 0], [1])
            elif name == 'Реальное дифференцирующее звено':
                unit = matlab.tf([k, 0], [t, 1])
        else:
            print(color.Fore.RED + '\nПожалуйста, введите числовое значение!')
            needNewChoice = True
    return unit

def graph (num, title, y, x):
    pyplot.subplot(2, 1, num)
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

[y,x] = matlab.step(unit, timeLine) #переходная функция
graph(1, 'Переходная характеристика', y, x)
[y,x] = matlab.impulse(unit, timeLine) #импульсная функция
graph(2, 'Импульсная характеристика', y, x)

f = 100/(1000-100)/450/1000
k = matlab.freqs(unit, timeLine, f*2*math.pi)
pyplot.subplot(2,1,1)
pyplot.plot(f,abs(k)/max(abs(k))), grid
pyplot.subplot(2,1,2)
pyplot.plot(f, unwrap(angle(k))), grid

pyplot.show()


