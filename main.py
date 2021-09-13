import pyautogui
import time
with open("classcode.txt") as f:
    class_code_list = f.read().split("\n")

def click(image,alternate=None):
    while True:
        if pyautogui.locateOnScreen(image) is not None:
            pyautogui.click(image)
            break
        elif alternate is not None and pyautogui.locateOnScreen(alternate):
            pyautogui.click(alternate)
            break
        time.sleep(0.5)
    time.sleep(0.5)
for i in class_code_list:
    time.sleep(1)
    click("images/add.png")
    click("images/join_class.png")
    time.sleep(0.3)
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.write(i)
    time.sleep(1.5)
    click("images/button.png")
    click("images/img.png",alternate="images/img_1.png")
    pyautogui.write("https://classroom.google.com/")
    pyautogui.press("enter")
    time.sleep(1.5)