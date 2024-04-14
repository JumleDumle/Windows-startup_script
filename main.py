import os
from pywinauto import application
import firefox_setup_downloader
import setup_firefox

def main():
    firefox_setup_downloader.download()
    setup_firefox.setup()
    

if __name__ == '__main__':
    main()