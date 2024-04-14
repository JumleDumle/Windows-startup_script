from pywinauto import Application
# import find_text
import pyautogui
import time
import pyuac

def setup_firefox():
    #if not pyuac.isUserAdmin():
    #    pyuac.runAsAdmin()

    app = Application(backend="uia").start("firefox_setup.exe")
    time.sleep(5)
    app.print_control_identifiers()


setup_firefox()