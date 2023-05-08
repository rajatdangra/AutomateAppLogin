import time
import os
import pyautogui

# Path to the application executable
app_path = "C:\\Program Files (x86)\\Cisco\\Cisco AnyConnect Secure Mobility Client\\vpnui.exe"

# Open the application
os.startfile(app_path)

# Wait for the application to load
time.sleep(1)
# Log out
pyautogui.press('enter')
time.sleep(7)

# Exit the application
pyautogui.hotkey('alt', 'f4')
# Wait for the process to complete
time.sleep(1)