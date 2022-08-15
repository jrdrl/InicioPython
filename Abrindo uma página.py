import pyautogui
import pyperclip
import time
pyautogui.PAUSE = 0.8
pyautogui.alert("Entrando em site de otako")
pyautogui.hotkey("win", "2")
pyautogui.hotkey("ctrl", "t")
link = "https://animes.vision"
pyperclip.copy(link)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
print("Site de otako aberto com sucesso!!!")
"Clicando no episódio recém lançado de um anime qualquer"
time.sleep(3)
pyautogui.click(x=1914, y=504)
pyautogui.click(x=227, y=528)
time.sleep(2)
pyautogui.click(x=924, y=213)
pyautogui.press("f")
