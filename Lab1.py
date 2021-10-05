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
                    unit = matlab.tf([k, 0], [0.00001, 1])
            elif name == 'Реальное дифференцирующее звено':
                unit = matlab.tf([k, 0], [t, 1])
        else:
            print(color.Fore.RED + '\nПожалуйста, введите числовое значение!')
            needNewChoice = True
    return unit

def graph (num, title, y, x):
    pyplot.subplot(2, 2, num)
    pyplot.tight_layout()  #отступы между графиками
    pyplot.grid(True)
    if title == 'Переходная характеристика':
        pyplot.plot(x, y, 'red')
        pyplot.title(title)
        pyplot.ylabel('Magnitude')
        pyplot.xlabel('Time (s)')
    elif title == 'Импульсная характеристика':
        pyplot.plot(x, y, 'blue')
        pyplot.title(title)
        pyplot.ylabel('Magnitude')
        pyplot.xlabel('Time (s)')
    elif title == 'АЧХ':
        pyplot.plot(x, y, 'green')
        pyplot.title(title)
        pyplot.ylabel('Magnitude')
        pyplot.xlabel('Omega (rad/s)')
    elif title == 'ФЧХ':
        pyplot.plot(omega, phase * 180 / math.pi, 'yellow')
        pyplot.title(title)
        pyplot.ylabel('Phase (deg)')
        pyplot.xlabel('Omega (rad/s)')

unitName = choice()
unit = getUnit(unitName)


timeLine = []
for i in range(0, 10000):
    timeLine.append(i/1000)

omega = []
for i in range(0, 1000):
    omega.append(i/1000)

#переходная функция
[y,x] = matlab.step(unit, timeLine)
graph(1, 'Переходная характеристика', y, x)

#импульсная функция
[y,x] = matlab.impulse(unit, timeLine)
graph(3, 'Импульсная характеристика', y, x)

#АЧХ и ФЧХ
mag, phase, omega = matlab.freqresp(unit, omega)
graph(2, 'АЧХ', mag, omega)
graph(4, 'ФЧХ', omega, phase * 180 / math.pi)

pyplot.show()



