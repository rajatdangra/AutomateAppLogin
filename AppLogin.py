import time
import os
import pyautogui

# Path to the application executable
app_path = "C:\\Program Files (x86)\\Cisco\\Cisco AnyConnect Secure Mobility Client\\vpnui.exe"

# Open the application
os.startfile(app_path)

# Wait for the application to load
time.sleep(1)
pyautogui.press('enter')
time.sleep(10)

# Type the username and password and click the login button
pyautogui.typewrite('username')
pyautogui.press('enter')
time.sleep(2)
pyautogui.typewrite('password')
pyautogui.press('enter')

# Wait for the login process to complete
time.sleep(5)