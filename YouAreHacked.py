import os
import pyautogui
import time

pyautogui.hotkey("win", "r")
time.sleep(1)
pyautogui.write("notepad.exe")
pyautogui.press("enter")
time.sleep(3)
text="you are hacked"
for character in text:
    pyautogui.write(character)
pyautogui.hotkey("win", "r")
time.sleep(2)
pyautogui.write("cmd")
pyautogui.press("enter")
time.sleep(2)
pyautogui.hotkey("F11")
pyautogui.write("color a")
pyautogui.press("enter")
time.sleep(0.5)
pyautogui.write("dir/s")
pyautogui.press("enter")
time.sleep(5)
pyautogui.hotkey("ctrl", "c")
pyautogui.write("exit")
pyautogui.press("enter")
time.sleep(1)
os.system("shutdown /s /t 1") #This will shutdown the computer after 1 second, you can change the time if you want or completely remove it if you don't want it to shutdown
