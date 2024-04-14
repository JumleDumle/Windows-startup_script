import pyautogui
import pytesseract
import cv2
import numpy as np

# In case you're on Windows and pytesseract doesn't
# find your installation (Happened to me)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def find_coordinates_text(text, lang='en'):
    # Take a screenshot of the main screen
    screenshot = pyautogui.screenshot()

    # Convert the screenshot to grayscale
    img = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2GRAY)

    # Find the provided text (text) on the grayscale screenshot 
    # using the provided language (lang)
    data = pytesseract.image_to_data(img, lang=lang, output_type='data.frame')

    # Find the coordinates of the provided text (text)
    try:
        x, y = data[data['text'] ==
                    text]['left'].iloc[0], data[data['text'] == text]['top'].iloc[0]

    except IndexError:
        # The text was not found on the screen
        return None

    # Text was found, return the coordinates
    return (x, y)