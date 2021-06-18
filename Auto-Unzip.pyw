DOWNLOADS_FOLDER = r'C:\Users\Andre\Downloads'
ZIP_EXTENSION = '.zip'
UPDATE_DELAY = 1

import os
import time
import zipfile
from win10toast import ToastNotifier

toast = ToastNotifier()
toast.show_toast('Auto-Unzip', 'The process has started', duration=5)

while True:
    for file in os.listdir(DOWNLOADS_FOLDER):
        if file.endswith(ZIP_EXTENSION):
            full_path = DOWNLOADS_FOLDER + '\\' + file
            with zipfile.ZipFile(full_path) as zip:
                zip.extractall(full_path[:-3])
            os.remove(full_path)    
            os.startfile(full_path[:-3])
            print(f'Extracted {file}')
    time.sleep(UPDATE_DELAY)
