import pyautogui
import time
import csv
import os


time.sleep(5)
pyautogui.hotkey('win', 'r') 
pyautogui.hotkey('ctrl', 'a')
time.sleep(2)
pyautogui.hotkey('del')
time.sleep(2)
pyautogui.typewrite('iexplore http://ebs.example.com:8000')
time.sleep(5)
pyautogui.hotkey('return')
time.sleep(5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('del')
pyautogui.typewrite('shakher')
pyautogui.hotkey('tab')
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('del')
pyautogui.typewrite('welcome')
pyautogui.hotkey('return')
 
time.sleep(5)
gl_vo_usa_location = pyautogui.locateOnScreen('gl_vo_usa.png')
gl_vo_usa_point = pyautogui.center(gl_vo_usa_location)
gl_vo_usa_x, gl_vo_usa_y = gl_vo_usa_point
pyautogui.click(gl_vo_usa_x, gl_vo_usa_y)
 
time.sleep(3)
setup_location = pyautogui.locateOnScreen('setup.png')
setup_point = pyautogui.center(setup_location)
setup_x, setup_y = setup_point
pyautogui.click(setup_x, setup_y)
 
time.sleep(3)
currencies_location = pyautogui.locateOnScreen('currencies.png')
currencies_point = pyautogui.center(currencies_location)
currencies_x, currencies_y = currencies_point
pyautogui.click(currencies_x, currencies_y)
 
time.sleep(3)
rates_location = pyautogui.locateOnScreen('rates.png')
rates_point = pyautogui.center(rates_location)
rates_x, rates_y = rates_point
pyautogui.click(rates_x, rates_y)
 
time.sleep(3)
daily_location = pyautogui.locateOnScreen('daily.png')
daily_point = pyautogui.center(daily_location)
daily_x, daily_y = daily_point
pyautogui.click(daily_x, daily_y)
 
time.sleep(3)
pyautogui.hotkey('shift', 'tab')
pyautogui.press('space')
pyautogui.press('return')
 
time.sleep(2)
pyautogui.hotkey('shift', 'tab')
pyautogui.press('space')
pyautogui.press('return')
 
time.sleep(30)
 
with open('sample.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        time.sleep(1)
        pyautogui.typewrite(row[0])
        time.sleep(1)
        pyautogui.press('tab')
        time.sleep(1)
        pyautogui.typewrite(row[1])
        time.sleep(1)
        pyautogui.press('tab')
        pyautogui.typewrite(row[2])
        time.sleep(1)
        pyautogui.press('tab')
        pyautogui.typewrite(row[3])
        time.sleep(1)
        pyautogui.press('tab')
        pyautogui.typewrite(row[4])
        time.sleep(1)
        pyautogui.press('tab')
        pyautogui.typewrite(row[5])
        time.sleep(1)
        pyautogui.press('tab')
        time.sleep(1)
    
    time.sleep(2) 
    pyautogui.hotkey('ctrl', 's')
    
    time.sleep(2)
    pyautogui.press('f11')
    
    time.sleep(2)
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.typewrite('26-MAY-2020')
    
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'f11')
    
pyautogui.alert('Process completed!')