from pywinauto import Application
# import find_text
import pyautogui
import time



# Start firefox setup
app = Application().start("firefox_setup_old.exe")

# deal with priviledge prompt
# wait for priviledge prompt
time.sleep(8)
# find "next" button and click it
yes_button = pyautogui.locateOnScreen('yes.png')
yes_point = pyautogui.center(yes_button)
pos_x, pos_y = yes_point
pyautogui.click(pos_x, pos_y)


"""
app.MozillaFirefoxSetup.button_select("next")
app.MozillaFirefoxSetup.OK.click()
"""