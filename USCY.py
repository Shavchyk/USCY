import pyautogui as pyag
import time as t
from screeninfo import get_monitors

monitors = get_monitors()
for monitor in monitors:
    width =  monitor.width
    height = monitor.height
print(width,height)
nx1 = 10.417
ny1 = 54.926
nx2 = 80.729
ny2 = 42.593
nx3 = 80.729
ny3 = 55.556
nx4 = 57.292
ny4 = 55.556

x1 = int(width * nx1 / 100)
y1 = int(height * ny1 / 100)
x2 = int(width * nx2 / 100)
y2 = int(height * ny2 / 100)
x3 = int(width * nx3 / 100)
y3 = int(height * ny3 / 100)
x4 = int(width * nx4 / 100)
y4 = int(height * ny4 / 100)

#root values
# x1 = 200 
# y1 = 550 
# x2 = 1550 
# y2 = 460 
# x3 = 1550 
# y3 = 600 
# x4 = 1100 
# y4 = 600 

t.sleep(0.5)
for i in range(10):
    pyag.moveTo(x1, y1)
    t.sleep(0.3)
    pyag.click(button='left')
    pyag.moveTo(x2, y2)
    t.sleep(0.3)
    pyag.click(button='left')
    pyag.moveTo(x3, y3)
    t.sleep(0.3)
    pyag.click(button='left')
    pyag.moveTo(x4, y4)
    t.sleep(0.3)
    pyag.click(button='left')
