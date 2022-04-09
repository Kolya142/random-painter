import pyautogui
import random
import time
import os
while2 = input("points=") #points
print("2 sec")
time.sleep(1)
os.system('cls')
print("1 sec")
time.sleep(1)
os.system('cls')
os.system("start mspaint.exe")
time.sleep(1.25)
pyautogui.click(751, 152)
pyautogui.click(774, 305)
time.sleep(0.25)
pyautogui.click(775, 305)
time.sleep(0.25)
while1 = 0
while2 = int (while2) #convert to "int"
while while1 < while2:
    color = random.randrange(1,5)
    if color == 1:
        pyautogui.click(958,97)
    elif color == 2:
        pyautogui.click(993,97)
    elif color == 3:
        pyautogui.click(1039,103)
    elif color == 4:
        pyautogui.click(887,97)
    elif color == 5:
        pyautogui.click(1021,99)
    elif color == 6:
        pyautogui.click(879,122)
    time.sleep(0.25)
    x,y = pyautogui.position()
    x1 = random.randrange(3,1831)
    y1 = random.randrange(184,1022)
    if x == 0:
        if y == 0:
            break
    pyautogui.moveTo(x1,y1,duration = 0.00001,tween = pyautogui.easeInOutQuad)
    pyautogui.click()
    while1 += 1
    print(str (while1) + " from " + str (while2))
os.system("pause >nul")