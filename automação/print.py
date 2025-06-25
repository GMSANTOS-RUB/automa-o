import pyautogui

pyautogui.press('win')
pyautogui.sleep(1)
pyautogui.write('google chrome', intervalo= 0.2)
pyautogui.press('enter') 
pyautogui.sleep(2)
pyautogui.write('senai - santana de parnaiba', intervalo= 0.9)
pyautogui.press('enter')
pyautogui.sleep(1)
pyautogui.moveTo(906,507, duration= 0.4)
pyautogui.click()
pyautogui.sleep(1)
pyautogui.hotkey('shift', 'win', 's' )
pyautogui.sleep(1)
pyautogui.moveTo(811,226, duration=0.5)

pyautogui.mousedown()
pyautogui.moveTo(1751,1025, duration=0.5)
pyautogui.mouseUp()
pyautogui.sleep(2)
pyautogui.press('win')
pyautogui.sleep(1)
pyautogui.write('paint', interval=0.2)
pyautogui.press('enter')
pyautogui.sleep(2)
pyautogui.hotkey('ctrl', 'v')

# FIm