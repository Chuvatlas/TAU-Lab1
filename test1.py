import matplotlib.pyplot as pyplot
import control.matlab as matlab
import numpy as numpy
import math
import colorama as color

def graph (num, title, y, x):
    pyplot.subplot(2, 2, num)
    pyplot.tight_layout()  #отступы между графиками
    pyplot.grid(True)
    if title == 'Переходная характеристика':
        pyplot.plot(x, y, 'red')
        pyplot.title(title)
        pyplot.ylabel('Magnitude')
        pyplot.xlabel('Time (s)')

unit = matlab.tf([21], [200, 105, 60, 1])

timeLine = []
for i in range(0, 10000):
    timeLine.append(i/1000)

omega = []
for i in range(0, 1000):
    omega.append(i/1000)

[y,x] = matlab.step(unit, timeLine)
graph(1, 'Переходная характеристика', y, x)
