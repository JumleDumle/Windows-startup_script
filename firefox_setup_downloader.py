import os
import requests # type: ignore

def download():
    url = "https://download-installer.cdn.mozilla.net/pub/firefox/releases/99.0/win64/en-US/Firefox%20Setup%2099.0.exe"
    response = requests.get(url)
    open("firefox_setup_new.exe", "wb").write(response.content)