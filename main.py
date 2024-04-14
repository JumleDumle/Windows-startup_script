import os
from pywinauto import application
import firefox_setup_downloader

def main():
    firefox_setup_downloader.download()
    

if __name__ == '__main__':
    main()