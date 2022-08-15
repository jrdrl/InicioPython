"""Adiciona menssagem repetida ao whatsapp de forma simples OBS: Sempre o quarto contato da lista pelo pc"""
import time
import pyautogui

pyautogui.hotkey("win", "2")
time.sleep(2)
pyautogui.click(x=22, y=206)
time.sleep(6)
pyautogui.click(x=152, y=478)
count = 0
while count < 40:
    pyautogui.write("GG")
    pyautogui.press("enter")
    count = count + 1
